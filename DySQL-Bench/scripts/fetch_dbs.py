#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
fetch_dbs.py - Download one or more SQLite DB files from Hugging Face datasets repo
Usage examples:
  # 列出可用环境
  python fetch_dbs.py --list

  # 拉取全部
  python fetch_dbs.py --all

  # 只拉 pagila 和 retail
  python fetch_dbs.py pagila retail

  # 指定其他 revision（tag/branch/commit）
  python fetch_dbs.py --revision main --all
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, Any, Tuple, List

try:
    from huggingface_hub import hf_hub_download
except Exception as e:
    raise SystemExit(
        "Missing dependency: huggingface_hub\n"
        "Install with: pip install huggingface_hub"
    ) from e


# ---- Config defaults (可以改成你的默认) ----
DEFAULT_REPO_ID = "gtysssp/Real-World-SQL-Bench-Databases"  # HF datasets repo
DEFAULT_REPO_TYPE = "dataset"
DEFAULT_MANIFEST = "./scripts/db_manifest.json"


def load_manifest(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 兼容两种结构：
    # 1) { env: { "hf_path": "hf://datasets/ORG/REPO/dbs/x.sqlite", "local_path": "..." } }
    # 2) { env: "dbs/x.sqlite" }  # 纯相对路径（若你以后想简化）
    norm: Dict[str, Dict[str, str]] = {}
    for env, v in data.items():
        if isinstance(v, str):
            hf_path = v  # 可能是 "dbs/x.sqlite" 或 "hf://datasets/.../dbs/x.sqlite"
            local_path = f"dysql_bench/envs/{env}/data/{Path(hf_path).name}"
        else:
            hf_path = v.get("hf_path") or v.get("hf") or v.get("path")
            local_path = v.get("local_path") or v.get("local") or v.get("dest")
        if not hf_path or not local_path:
            raise ValueError(f"Manifest entry for '{env}' is incomplete: {v}")

        # 统一把 hf_path 解析成：repo 内相对路径（给 hf_hub_download 的 filename）
        # 支持两类写法：
        #   - "dbs/pagila.sqlite"
        #   - "hf://datasets/org/repo/dbs/pagila.sqlite"
        if hf_path.startswith("hf://"):
            # 形如 hf://datasets/<org>/<repo>/<subpath...>
            parts = Path(hf_path.replace("hf://", "", 1)).parts
            # 期望 ["datasets", org, repo, ...subpath]
            if len(parts) < 4 or parts[0] != "datasets":
                raise ValueError(f"Unsupported hf_path format: {hf_path}")
            # 记录下 repo 和内部相对路径（但我们仍允许用命令行 --repo 覆盖）
            subpath = Path(*parts[3:]).as_posix()
            filename_rel = subpath
        else:
            # 直接是 repo 内相对路径
            filename_rel = Path(hf_path).as_posix()

        norm[env] = {"filename_rel": filename_rel, "local_path": local_path}
    return norm


def ensure_parent_dir(p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)


def download_one(
    repo_id: str,
    repo_type: str,
    revision: str,
    filename_rel: str,
    local_path: str,
    dry_run: bool = False,
) -> str:
    """
    Download a single file from HF datasets repo into the exact local_path.
    We use hf_hub_download with local_dir to place a real copy (no symlink).
    """
    dst = Path(local_path).resolve()
    ensure_parent_dir(dst)

    if dry_run:
        print(f"[DRY-RUN] would download: {repo_id}:{filename_rel} -> {dst}")
        return str(dst)

    # 将文件落到其父目录，并保持文件名一致
    # local_dir_use_symlinks=False => 生成真实文件，非软链接，便于后续直接使用/打包
    local_dir = str(dst.parent)
    res_path = hf_hub_download(
        repo_id=repo_id,
        repo_type=repo_type,
        filename=filename_rel,
        revision=revision,
        local_dir=local_dir,
        local_dir_use_symlinks=False,
    )
    # hf_hub_download 会把文件保存为 local_dir/filename_rel 的相对结构；
    # 我们期望最终路径就是 dst（同名），因此无需额外移动。
    print(f"[OK] {filename_rel} -> {res_path}")
    return res_path


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Download one or more DB files from a Hugging Face datasets repo "
                    "according to db_manifest.json"
    )
    ap.add_argument("--repo", default=DEFAULT_REPO_ID,
                    help=f"Hugging Face repo id (default: {DEFAULT_REPO_ID})")
    ap.add_argument("--repo-type", default=DEFAULT_REPO_TYPE,
                    help=f"repo type for HF hub (default: {DEFAULT_REPO_TYPE})")
    ap.add_argument("--revision", default="main",
                    help="branch/tag/commit to pin (default: main)")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST,
                    help=f"manifest json path (default: {DEFAULT_MANIFEST})")

    group = ap.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="download all entries in manifest")
    group.add_argument("--list", action="store_true", help="list available env names")

    ap.add_argument("envs", nargs="*", help="env names to download (e.g., pagila retail)")
    ap.add_argument("--dry-run", action="store_true", help="print actions without downloading")
    return ap.parse_args()


def main():
    args = parse_args()
    manifest = load_manifest(args.manifest)

    if args.list:
        print("Available environments:")
        for k in manifest.keys():
            print(f"  - {k}")
        return

    if args.all:
        targets = list(manifest.keys())
    else:
        if not args.envs:
            raise SystemExit("No env specified. Use --all or pass env names, or --list to view.")
        unknown = [e for e in args.envs if e not in manifest]
        if unknown:
            raise SystemExit(f"Unknown env(s) in args: {unknown}\n"
                             f"Try --list to see available ones.")
        targets = args.envs

    print(f"Repo: {args.repo} (type={args.repo_type}, rev={args.revision})")
    print(f"Targets: {targets}")

    for env in targets:
        entry = manifest[env]
        filename_rel = entry["filename_rel"]
        local_path = entry["local_path"]
        download_one(
            repo_id=args.repo,
            repo_type=args.repo_type,
            revision=args.revision,
            filename_rel=filename_rel,
            local_path=local_path,
            dry_run=args.dry_run,
        )

    print("Done.")


if __name__ == "__main__":
    main()
