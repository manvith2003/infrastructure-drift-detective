from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from app.core.database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, default="user")
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cloud_provider = Column(String, nullable=False)  # aws / gcp / azure
    repo_url = Column(String, nullable=True)
    tf_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects")

    drift_records = relationship("DriftRecord", back_populates="project")
    state_snapshots = relationship("StateSnapshot", back_populates="project")


class StateSnapshot(Base):
    __tablename__ = "state_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    tf_state = Column(JSON, nullable=True)
    actual_state = Column(JSON, nullable=True)

    snapshot_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="state_snapshots")
    drift_records = relationship("DriftRecord", back_populates="snapshot")


class DriftRecord(Base):
    __tablename__ = "drift_records"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    snapshot_id = Column(Integer, ForeignKey("state_snapshots.id"), nullable=False)

    severity = Column(String, nullable=False)  # low / medium / high
    status = Column(String, default="open")    # open / acknowledged / remediated / ignored
    summary = Column(String, nullable=True)
    detected_at = Column(DateTime, default=datetime.utcnow)
    explanation = Column(String, nullable=True)

    project = relationship("Project", back_populates="drift_records")
    snapshot = relationship("StateSnapshot", back_populates="drift_records")

    remediation_actions = relationship("RemediationAction", back_populates="drift")
    notifications = relationship("Notification", back_populates="drift")


class RemediationAction(Base):
    __tablename__ = "remediation_actions"

    id = Column(Integer, primary_key=True, index=True)
    drift_id = Column(Integer, ForeignKey("drift_records.id"), nullable=False)

    action_type = Column(String, nullable=False)  # update_iac / revert_infra / investigate
    status = Column(String, default="pending")    # pending / applied / failed
    executed_at = Column(DateTime, nullable=True)

    drift = relationship("DriftRecord", back_populates="remediation_actions")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    drift_id = Column(Integer, ForeignKey("drift_records.id"), nullable=False)

    channel = Column(String, nullable=False)  # slack / jira / email
    status = Column(String, default="sent")   # sent / failed
    sent_at = Column(DateTime, default=datetime.utcnow)

    drift = relationship("DriftRecord", back_populates="notifications")
