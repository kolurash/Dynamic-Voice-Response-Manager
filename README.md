# Dynamic Voice Response Manager

## Overview
Dynamic Voice Response Manager is a Python-based Text-to-Speech (TTS) project that controls speaking flow dynamically to create smooth, natural, and human-like voice responses.

This project was developed as part of a Prompt Engineering Internship Task.

---

## Objective
To control speaking flow dynamically using:

- Natural pauses
- Smooth pacing
- Interruption support
- Context-aware responses
- Non-robotic voice interaction

---

## Features

### Dynamic Greetings
- Responds to greetings naturally

### Smart Responses
Supports multiple user inputs like:

- hello
- how are you
- your name
- who created you
- what can you do
- thank you
- good morning
- good night
- tell me a joke
- tell me a story
- quote
- motivate me
- compliment me
- sing a song
- stop
- bye

---

## Technologies Used

- Python
- pyttsx3
- Time Module

---

## Project Structure

```bash
DynamicVoiceResponseManager/
│── main.py
│── voice_controller.py
│── config.py
│── README.md
```

---

## Installation

Install dependency:

```bash
pip install pyttsx3
```

---

## Run the Project

```bash
python main.py
```

---

## Example Interaction

**Input:**
```bash
hello
```

**Output:**
```bash
Hello, nice to talk with you.
```

---

**Input:**
```bash
how are you
```

**Output:**
```bash
I am doing well, thank you for asking.
```

---

**Input:**
```bash
tell me a story
```

**Output:**
Assistant tells a short motivational story.

---

**Input:**
```bash
quote
```

**Output:**
Assistant speaks an inspirational quote.

---

## Key Achievements

- Built a dynamic TTS voice manager
- Avoided robotic speech output
- Added intelligent multi-response handling
- Implemented interruption support
- Improved natural conversational flow

---

## Internship Task Details

**Module:** TTS Pipeline  
**Difficulty:** Medium  
**Duration:** 1 Week

---

## Outcome

Successfully developed a Dynamic Voice Response Manager capable of generating smooth and intelligent voice responses dynamically.

---
