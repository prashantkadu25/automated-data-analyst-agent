# src/core/session_service.py
import uuid, time
from loguru import logger

class InMemorySessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id=None):
        sid = str(uuid.uuid4())
        self.sessions[sid] = {
            "user_id": user_id,
            "created_at": time.time(),
            "artifacts": {},
            "history": []
        }
        logger.info(f"Session created {sid}")
        return sid

    def add_artifact(self, session_id, name, value):
        self.sessions[session_id]["artifacts"][name] = value

    def append_history(self, session_id, entry):
        self.sessions[session_id]["history"].append(entry)

    def get_session(self, session_id):
        return self.sessions.get(session_id)
