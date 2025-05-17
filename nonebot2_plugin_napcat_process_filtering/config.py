#插件本身已经有默认值，可以根据.env.prod修改，又因为这个脚本基于napcat只能在qq使用
#config.py仅作为示范作用
'''

from pydantic import BaseModel

class Config(BaseModel):
    api_base: str = "http://127.0.0.1:3000"
    interval: int = 3600
    count: int = 1
    enable_logging: bool = True
    log_file: str = "approved_requests.txt"
    
'''