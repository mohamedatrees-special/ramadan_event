{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "700f3b7a-82a0-408f-b146-a8272c022cf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Database created successfully!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "# مسار قاعدة البيانات\n",
    "DB_PATH = \"event.db\"\n",
    "\n",
    "# إنشاء اتصال بالقاعدة\n",
    "conn = sqlite3.connect(DB_PATH)\n",
    "c = conn.cursor()\n",
    "\n",
    "# إنشاء جدول المشاركين\n",
    "c.execute(\"\"\"\n",
    "CREATE TABLE IF NOT EXISTS participants(\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "    name TEXT NOT None,\n",
    "    date_of_birth DATE NOT None,\n",
    "    gender TEXT NOT None,\n",
    "    package TEXT NOT None,\n",
    "    phone INTEGER NOT None,\n",
    "    national_id TEXT NOT None,\n",
    "    payment_proof TEXT\n",
    ")\n",
    "\"\"\")\n",
    "\n",
    "conn.commit()\n",
    "conn.close()\n",
    "print(\"Database created successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9d834ffd-9943-4073-b278-b91deaf0a67a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10 (Sign Project)",
   "language": "python",
   "name": "python310"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
