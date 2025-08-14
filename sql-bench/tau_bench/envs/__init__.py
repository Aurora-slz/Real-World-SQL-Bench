# Copyright Sierra

from typing import Optional, Union
from tau_bench.envs.base import Env
from tau_bench.envs.user import UserStrategy

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
        from tau_bench.envs.retail import MockRetailDomainSQLEnv
        return MockRetailDomainSQLEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "airline":
        from tau_bench.envs.airline import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            #user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "eu_soccer":
        from tau_bench.envs.eu_soccer import MockEUSoccerEnv
        return MockEUSoccerEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    elif env_name == "music":
        from tau_bench.envs.music import MockMusicEnv
        return MockMusicEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_split=task_split,
            task_index=task_index,
            thread_id=thread_id
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}")
