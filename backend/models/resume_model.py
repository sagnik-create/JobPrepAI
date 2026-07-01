from datetime import datetime
import uuid

class Resume:
    def __init__(
        self,
        file_name,
        file_path,
        parsed_data,
        ai_data=None,
        insights=None,
        is_active=True
    ):
        self.id = str(uuid.uuid4())
        self.file_name = file_name
        self.file_path = file_path
        self.uploaded_at = datetime.utcnow().isoformat()
        self.parsed_data = parsed_data
        self.ai_data = ai_data or {}
        self.insights = insights or []
        self.is_active = is_active

    def to_dict(self):
        return {
            "id": self.id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "uploaded_at": self.uploaded_at,
            "parsed_data": self.parsed_data,
            "ai_data": self.ai_data,
            "insights": self.insights,
            "is_active": self.is_active
        }