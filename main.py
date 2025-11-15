from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from pydantic import BaseModel, EmailStr
import warnings

# Suppress pydantic config warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._config")


# =====================================================
# DATABASE CONFIGURATION (Single DB for Members + Contacts)
# =====================================================
DATABASE_URL = "sqlite:///./membership.db"  # Unified SQLite DB

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# =====================================================
# DEPENDENCY
# =====================================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =====================================================
# FASTAPI INITIALIZATION
# =====================================================
app = FastAPI(title="Membership & Contact API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# SQLALCHEMY MODELS
# =====================================================
class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=True)
    country = Column(String, index=True, nullable=False)
    message = Column(String, index=True, nullable=True)


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)


# =====================================================
# PYDANTIC SCHEMAS
# =====================================================
# ---- Member ----
class MemberCreate(BaseModel):
    name: str
    email: str
    phone: str
    country: str
    city: Optional[str] = None
    message: Optional[str] = None


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    message: Optional[str] = None


class MemberOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    country: str
    city: Optional[str]
    message: Optional[str]

    class Config:
        orm_mode = True


# ---- Contact Form ----
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str


# =====================================================
# CREATE TABLES
# =====================================================
Base.metadata.create_all(bind=engine)


# =====================================================
# MEMBER API ROUTES
# =====================================================
@app.post("/members/", response_model=MemberOut)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    """Create a new member"""
    existing_member = db.query(Member).filter(Member.email == member.email).first()
    if existing_member:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_member = Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@app.get("/members/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    """Get a single member by ID"""
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.put("/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, updated: MemberUpdate, db: Session = Depends(get_db)):
    """Update a member by ID"""
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    for field, value in updated.dict(exclude_unset=True).items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)
    return member


@app.get("/members/", response_model=List[MemberOut])
def list_members(db: Session = Depends(get_db)):
    """List all members"""
    return db.query(Member).all()


# =====================================================
# CONTACT FORM API ROUTES
# =====================================================
@app.post("/contact/")
def create_contact(contact: ContactForm, db: Session = Depends(get_db)):
    """Store contact form message"""
    db_contact = ContactMessage(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return {"message": "Contact form submitted successfully"}


@app.get("/contact/")
def get_contacts(db: Session = Depends(get_db)):
    """Fetch all contact form submissions"""
    contacts = db.query(ContactMessage).all()
    return {"contacts": contacts}
