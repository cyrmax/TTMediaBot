from typing import Dict, List, Union

from pydantic import BaseModel


class GeneralModel(BaseModel):
    language: str = "en"
    send_channel_messages: bool = True
    cache_file_name: str = "TTMediaBotCache.dat"
    blocked_commands: List[str] = []
    delete_uploaded_files_after: int = 300
    time_format: str = r"%H:%M"


class SoundDevicesModel(BaseModel):
    output_device: int = 0
    input_device: int = 0


class PlayerModel(BaseModel):
    default_volume: int = 50
    max_volume: int = 100
    volume_fading: bool = True
    volume_fading_interval: float = 0.025
    seek_step: int = 5
    player_options: dict = {}


class TeamTalkUserModel(BaseModel):
    admins: List[str] = ["admin"]
    banned_users: List[str] =  []


class EventHandlingModel(BaseModel):
    load_event_handlers: bool = False
    event_handlers_file_name: str = "event_handlers.py"


class TeamTalkModel(BaseModel):
    hostname: str = "localhost"
    tcp_port: int = 10333
    udp_port: int = 10333
    encrypted: bool = False
    nickname: str = "TTMediaBot"
    status: str = ""
    gender: str = "n"
    username: str = ""
    password: str = ""
    channel: Union[int, str] = "/"
    channel_password: str = ""
    license_name: str = ""
    license_key: str = ""
    reconnection_attempts: int = -1
    reconnection_timeout: int = 10
    users: TeamTalkUserModel = TeamTalkUserModel()
    event_handling: EventHandlingModel = EventHandlingModel()


class ServicesModel(BaseModel):
    available_services: Dict[str, dict] = {"vk": {"token": ""}, "yt": {}}
    default_service: str = "vk"


class LoggerModel(BaseModel):
    log: bool = True
    level: str = "INFO"
    format: str = "%(levelname)s [%(asctime)s]: %(message)s in %(threadName)s file: %(filename)s line %(lineno)d function %(funcName)s"
    mode: Union[int, str] = "File"
    file_name: str = "TTMediaself.log"
    max_file_size: int = 0
    backup_count: int = 0


class ShorteningModel(BaseModel):
    shorten_links: bool = False
    service: str = "Bitly"
    service_token: str = ""



class ConfigModel(BaseModel):
    general: GeneralModel = GeneralModel()
    sound_devices: SoundDevicesModel = SoundDevicesModel()
    player: PlayerModel = PlayerModel()
    teamtalk: TeamTalkModel = TeamTalkModel()
    services: ServicesModel = ServicesModel()
    logger: LoggerModel = LoggerModel()
    shortening: ShorteningModel = ShorteningModel()
