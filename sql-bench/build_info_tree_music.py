import json
import sqlite3
import os
import time
from collections import defaultdict
from tqdm import tqdm


def build_info_tree(base_dir="local_sqlite", output_dir="."):
    start_time = time.time()
    db_path = os.path.join(base_dir, "music.sqlite")
    conn = sqlite3.connect(db_path)
    # 性能优化
    conn.execute('PRAGMA synchronous = OFF')
    conn.execute('PRAGMA journal_mode = MEMORY')
    cursor = conn.cursor()

    def fetch_table(name):
        cursor.execute(f"PRAGMA table_info({name})")
        header = {column[1]: column[0] for column in cursor.fetchall()} # 列名: 列号
        cursor.execute(f"SELECT * FROM {name}")
        rows = cursor.fetchall()
        return header, rows
    
    invoiceline_hdr, invoiceline_rows = fetch_table("InvoiceLine")
    invoice_hdr, invoice_rows = fetch_table("Invoice")
    customer_hdr, customer_rows = fetch_table("Customer")
    employee_hdr, employee_rows = fetch_table("Employee")
    playlisttrack_hdr, playlisttrack_rows = fetch_table("PlaylistTrack")
    playlist_hdr, playlist_rows = fetch_table("Playlist")
    track_hdr, track_rows = fetch_table("Track")
    album_hdr, album_rows = fetch_table("Album")
    artist_hdr, artist_rows = fetch_table("Artist")
    genre_hdr, genre_rows = fetch_table("Genre")
    mediatype_hdr, mediatype_rows = fetch_table("MediaType")

    # 通过InvoiceId索引InvoiceLine
    invoiceline_map = defaultdict(list)
    for row in invoiceline_rows:
        invoice_id = row[invoiceline_hdr["InvoiceId"]]
        if invoice_id is None: continue
        invoice_info = {col: row[idx] for idx, col in enumerate(invoiceline_hdr)}
        invoiceline_map[invoice_id].append(invoice_info)

    # invoiceline_map = {
    #     row[invoiceline_hdr["InvoiceId"]]: {
    #         col: row[idx] for idx, col in enumerate(invoiceline_hdr)
    #         if col != "InvoiceId"
    #     }
    #     for row in invoiceline_rows
    # }

    # 通过InvoiceId索引Invoice
    invoice_map = {
        row[invoice_hdr["InvoiceId"]]: {
            col: row[idx] for idx, col in enumerate(invoice_hdr)
            #if col != "InvoiceId"
        }
        for row in invoice_rows
    }

    # 通过CustomerId索引Customer
    customer_map = {
        row[customer_hdr["CustomerId"]]: {
            col: row[idx] for idx, col in enumerate(customer_hdr)
            #if col != "CustomerId"
        }
        for row in customer_rows
    }

    # 通过EmployeeId索引Employee
    employee_map = {
        row[employee_hdr["EmployeeId"]]: {
            col: row[idx] for idx, col in enumerate(employee_hdr)
            #if col != "EmployeeId"
        }
        for row in employee_rows
    }
    
    # 通过TrackId索引PlaylistTrack
    playlisttrack_map = {
        row[playlisttrack_hdr["TrackId"]]: {
            col: row[idx] for idx, col in enumerate(playlisttrack_hdr)
            #if col != "TrackId"
        }
        for row in playlisttrack_rows
    }

    # 通过PlaylistId索引Playlist
    playlist_map = {
        row[playlist_hdr["PlaylistId"]]: {
            col: row[idx] for idx, col in enumerate(playlist_hdr)
            #if col != "PlaylistId"
        }
        for row in playlist_rows
    }

    # 通过TrackId索引Track
    track_map = {
        row[track_hdr["TrackId"]]: {
            col: row[idx] for idx, col in enumerate(track_hdr)
            #if col != "TrackId"
        }
        for row in track_rows
    }

    # 通过AlbumId索引Album
    album_map = {
        row[album_hdr["AlbumId"]]: {
            col: row[idx] for idx, col in enumerate(album_hdr)
            #if col != "AlbumId"
        }
        for row in album_rows
    }

    # 通过ArtistId索引Artist
    artist_map = {
        row[artist_hdr["ArtistId"]]: {
            col: row[idx] for idx, col in enumerate(artist_hdr)
            #if col != "ArtistId"
        }
        for row in artist_rows
    }

    # 通过GenreId索引Genre
    genre_map = {
        row[genre_hdr["GenreId"]]: {
            col: row[idx] for idx, col in enumerate(genre_hdr)
            #if col != "GenreId"
        }
        for row in genre_rows
    }

    # 通过MediaTypeId索引MediaType
    mediatype_map = {
        row[mediatype_hdr["MediaTypeId"]]: {
            col: row[idx] for idx, col in enumerate(mediatype_hdr)
            #if col != "MediaTypeId"
        }
        for row in mediatype_rows
    }

    tree = []
    customer_id_to_idx = {} # 记录已经处理过的customer

    # 注: 一个customer_id对应多个invoice_id, 一个invoice_id对应多个invoiceline_id
    for invoice_id, invoice_info in tqdm(invoice_map.items(), desc="处理数据", unit="条"):
        invoicelines = invoiceline_map[invoice_id]          # 是Invoice_id对应的所有InvoiceLine构成的列表
        customer_id = invoice_info["CustomerId"]
        customer_info = customer_map[customer_id]
        employee_info = employee_map[customer_info["SupportRepId"]]

        # 将customer表格中的supportrepo信息加入到customer信息中
        customer_info['employee_info'] = employee_info

        # 将invoiceline表格中的信息加入到invoice信息中
        invoice_info['invoiceline_info'] = invoicelines

        if customer_id not in customer_id_to_idx:
            row = {
                    "customer_info": customer_info,
                    "track_info": [],
                    "invoice_info": []
                }
            customer_id_to_idx[customer_id] = len(tree)
            tree.append(row)
        
        row = tree[customer_id_to_idx[customer_id]]
        row['invoice_info'].append(invoice_info)

        # 将Track, PlayList, Album, Artist, Genre, MediaType的信息加入到Track中
        for invoiceline in invoicelines:
            # 从InvoiceLine表格读出TrackId, 以及当前TrackId所对应的表格中的信息
            track_id = invoiceline["TrackId"]
            track_info = track_map[track_id]

            # 从PlaylistTrack表格读出PlaylistId, 以及当前PlaylistId所对应的表格中的信息合并到track_info中
            playlist_id = playlisttrack_map[track_id]["PlaylistId"]
            playlist_info = playlist_map[playlist_id]
            track_info['playlist_info'] = ({"PlaylistId": playlist_id} | playlist_info)

            # 从Track表格读出AlbumId, 以及当前AlbumId所对应的表格中的信息合并到track_info中
            album_id = track_info["AlbumId"]
            album_info = album_map[album_id]
            track_info['album_info'] = album_info

            # 从Albulm表格读出ArtistId, 以及当前ArtistId所对应的表格中的信息合并到track_info中
            artist_id = album_info["ArtistId"]
            artist_info = artist_map[artist_id]
            track_info['artist_info'] = artist_info

            # 从Track表格读出GenreId, 以及当前GenreId所对应的表格中的信息合并到track_info中
            genre_id = track_info["GenreId"]
            genre_info = genre_map[genre_id]
            track_info['genre_info'] = genre_info

            # 从Track表格读出MediaTypeId, 以及当前MediaTypeId所对应的表格中的信息合并到track_info中
            mediatype_id = track_info["MediaTypeId"]
            mediatype_info = mediatype_map[mediatype_id]
            track_info['mediatype_info'] = mediatype_info

            # 将track_info加入到customer_info['track_info']中
            row['track_info'].append(track_info)

    # 输出 JSONL
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, 'tree_music.jsonl')
    with open(out_path, 'w', encoding='utf-8') as fw:
        for record in tqdm(tree,  desc="写入数据", unit="条"):
            fw.write(json.dumps(record, ensure_ascii=False) + "\n")

    with open("example_music_customer_id_9.json", "w", encoding="utf-8") as f:
        json.dump(tree[8], f, indent=4)

    with open("example_music_customer_id_34.json", "w", encoding="utf-8") as f:
        json.dump(tree[33], f, indent=4)

    with open("example_music_customer_id_51.json", "w", encoding="utf-8") as f:
        json.dump(tree[50], f, indent=4)


    print(f"Built tree with {len(tree)} customers in {time.time()-start_time:.2f}s. Saved to {out_path}")



if __name__ == '__main__':
    build_info_tree()