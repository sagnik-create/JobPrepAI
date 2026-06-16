from datetime import datetime
import uuid

class Resume:
    def __init__(self,file_name, file_path, parsed_data):
        self.id = str(uuid.uuid4())
        self.file_name = file_name
        self.uploaded_at = datetime.utcnow().isoformat()
        self.parsed_data = parsed_data
        self.is_active = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "file_name": self.file_name,
            "uploaded_at": self.uploaded_at,
            "parsed_data": self.parsed_data,
            "is_active": self.is_active
        }
