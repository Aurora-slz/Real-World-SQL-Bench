# Copyright Sierra

from typing import Optional, Union
from dysql_bench.envs.base import Env
from dysql_bench.envs.user import UserStrategy

def get_env(
    env_name: str,
    user_strategy: Union[str, UserStrategy],
    user_model: str,
    user_model_api: str,
    task_split: str,
    task_index: Optional[int] = None,
    thread_id: int = None
) -> Env:
    if env_name == "retail":
        from dysql_bench.envs.retail import MockRetailDomainSQLEnv
        return MockRetailDomainSQLEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "eu_soccer":
        from dysql_bench.envs.eu_soccer import MockEUSoccerEnv
        return MockEUSoccerEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "music":
        from dysql_bench.envs.music import MockMusicEnv
        return MockMusicEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "bowling":
        from dysql_bench.envs.bowling import MockBowlingEnv
        return MockBowlingEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "entertainment":
        from dysql_bench.envs.entertainment import MockEntertainmentEnv
        return MockEntertainmentEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "pagila":
        from dysql_bench.envs.pagila import MockPagilaEnv
        return MockPagilaEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "chinook":
        from dysql_bench.envs.chinook import MockChinookEnv
        return MockChinookEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "car":
        from dysql_bench.envs.car import MockCarEnv
        return MockCarEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "cookbook":
        from dysql_bench.envs.cookbook import MockCookbookEnv
        return MockCookbookEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "human_resources":
        from dysql_bench.envs.human_resources import MockHumanResourcesEnv
        return MockHumanResourcesEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "ice_hockey":
        from dysql_bench.envs.ice_hockey import MockIceHockeyEnv
        return MockIceHockeyEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "law_episode":
        from dysql_bench.envs.law_episode import MockLawEpisodeEnv
        return MockLawEpisodeEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "retail_world":
        from dysql_bench.envs.retail_world import MockRetailWorldEnv
        return MockRetailWorldEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}")
