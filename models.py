from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Подсистема управления контентом (CMS)
class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    description = Column(String)

# Подсистема авторизации и учетных записей
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# Подсистема новостей и событий
class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    category = Column(String, index=True)
    date_posted = Column(DateTime(timezone=True), server_default=func.now())

# Подсистема академических программ и курсов
class AcademicProgram(Base):
    __tablename__ = 'academic_programs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    admission_requirements = Column(Text)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    academic_program_id = Column(Integer, ForeignKey('academic_programs.id'))
    academic_program = relationship('AcademicProgram', back_populates='courses')

AcademicProgram.courses = relationship('Course', order_by=Course.id, back_populates='academic_program')

# Подсистема онлайн-обучения
class OnlineCourse(Base):
    __tablename__ = 'online_courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    material_link = Column(String)
    test_link = Column(String)

# Подсистема поиска и фильтрации
class SearchIndex(Base):
    __tablename__ = 'search_index'

    id = Column(Integer, primary_key=True, index=True)
    content_type = Column(String, index=True)
    content_id = Column(Integer, index=True)
    content_text = Column(Text)

# Подсистема коммуникации и обратной связи
class CommunicationMessage(Base):
    __tablename__ = 'communication_messages'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='messages')
    content = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

User.messages = relationship('CommunicationMessage', order_by=CommunicationMessage.id, back_populates='user')

# Подсистема аналитики и мониторинга
class SiteAnalytics(Base):
    __tablename__ = 'site_analytics'

    id = Column(Integer, primary_key=True, index=True)
    page_name = Column(String, index=True)
    visits = Column(Integer)
    unique_visitors = Column(Integer)
