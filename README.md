# DWRag
# 1.RAC คือ <br>
คือ เทคนิคที่ช่วยเพิ่มความสามารถของระบบ AI และ Generative AI ย่อมาจาก “Retrieval Augmented Generation”  โดยการเชื่อมโยงระบบเข้ากับแหล่งข้อมูลภายนอก แทนที่จะอาศัยเฉพาะข้อมูลที่มีอยู่ในโมเดล AI เอง RAG จะนำ Prompt ที่ผู้ใช้งานป้อนเข้ามาไปค้นหาข้อมูลที่เกี่ยวข้องจากแหล่งข้อมูลภายนอก เช่น เว็บไซต์ ฐานข้อมูลภายในองค์กร หรือเอกสารเฉพาะทาง จากนั้นข้อมูลที่ค้นพบจะถูกนำมาใช้เพื่อสร้าง Prompt ประกอบการทำงานของ GPT เพื่อช่วยให้ AI สามารถสร้างคำตอบที่มีความถูกต้อง แม่นยำ และสอดคล้องกับบริบทที่เฉพาะเจาะจงมากยิ่งขึ้น <br>

# 2.MCP คือ <br>
คือ โปรโตคอลเปิดที่เป็นสากลที่มาตรฐานวิธีที่แอปพลิเคชั่นจัดเตรียมข้อมูลบริบทให้กับโมเดลภาษาขนาดใหญ่ (LLMs) มีความคล้ายคลึงกับ HTTP ที่อนุญาตให้เว็บไซต์เบราว์เซอร์ต่างๆแลกเปลี่ยนข้อมูลเดียวกัน <br>

# 3.LangChain <br>
คือ เฟรมเวิร์ก open source ที่สนับสนุนให้นักพัฒนาสามารถพัฒนาแอปพลิเคชั่น Generative AI ด้วยการเชื่อมโยงโมเดลภาษาขนาดใหญ่ เช่น OpenAI, Face ได้อย่างสะดวกและยืดหยุ่น <br>

# Steps in implementing RAG in Django with postgresql & pgvector <br>
1. ติดตั้งpgvector โดย พิมพ์comman wsl เพื่อเข้าubuntu แล้วติดตั้ง <br>
2. CREATE EXTENSION IF NOT EXISTS vector; และสร้างDjango Project และตั้งค่าPostgreSQLกับDjango<br>
3. สร้าง Model  Document  <br>
<h1>ตัวอย่งโค้ด</h1><br>
```python

from django.db import models
from pgvector.django import VectorField

class Document(models.Model):
    content = models.TextField()
    embedding = VectorField(dimensions=1536) ```
    
4. ทำการmakemigrat และ makemigration <br>


