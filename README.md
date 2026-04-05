# CRCCIMI FAMILY CAMP - Scoring System

A modern Django-based scoring system for CRCCIMI Family Camp events where participants are grouped by color teams.

## Features

- **Modern Professional Interface**: Clean, responsive design with gradient backgrounds and smooth animations
- **Color-Based Teams**: 7 default color teams (Red, Blue, Green, Yellow, Orange, Purple, Pink)
- **Staff Authentication**: Secure login system with professional interface for staff members only
- **Merit/Demerit System**: Add positive and negative points to teams
- **Real-time Scoreboard**: Live team rankings with automatic sorting and podium display
- **Responsive Design**: Mobile, tablet, and desktop friendly
- **Activity Tracking**: Complete history of all score entries with staff attribution

## Quick Start

### 1. Login Credentials
- **Username**: `admin`
- **Password**: `admin123`

### 2. Access the System
1. Open your browser and go to `http://127.0.0.1:8000`
2. Login with the staff credentials above
3. You'll be redirected to the dashboard

### 3. Enhanced Login Interface

The login page features:
- **Modern Design**: Gradient background with floating animations
- **Professional Branding**: CRCCIMI YOUTH CAMP logo and title
- **Enhanced UX**: Icon-based input fields with smooth transitions
- **Error Handling**: Clear error messages with shake animations
- **Responsive Layout**: Works perfectly on all devices
- **Security Indicators**: Visual cues for secure login and staff-only access

### 4. Basic Usage

#### Adding Merits (Positive Points)
1. Click "Add Merit" button (green) in the navigation
2. Select a team from the dropdown
3. Enter points (1-100)
4. Add a description explaining the reason
5. Click "Add Merit"

#### Adding Demerits (Negative Points)
1. Click "Add Demerit" button (red) in the navigation
2. Select a team from the dropdown
3. Enter points (1-100) - will be automatically converted to negative
4. Add a description explaining the reason
5. Click "Add Demerit"

#### Viewing Scores
- **Dashboard**: Shows team rankings and recent activity
- **Scoreboard**: Detailed rankings with podium display for top 3
- **Team Details**: Click on any team to see their complete score history

## System Structure

### Models
- **Team**: Represents color teams with name and color
- **ScoreEntry**: Individual merit/demerit entries with team, points, description, and timestamp

### Design Features
- **Modern UI/UX**: Professional gradient backgrounds, smooth animations, and micro-interactions
- **Professional Branding**: CRCCIMI FAMILY CAMP theme throughout the system
- **Visual Hierarchy**: Clear typography and spacing for optimal user experience
- **Responsive Design**: Mobile-first approach with tablet and desktop optimization
- **Accessibility**: Semantic HTML and ARIA-friendly design

### Key Features
- Points can be added anytime, not just during games
- Automatic score calculation and ranking
- Staff user tracking for all score entries
- Clean, intuitive interface using Tailwind CSS
- Professional animations and transitions

## Technical Details

- **Framework**: Django 6.0.3
- **Database**: SQLite (development)
- **Frontend**: Tailwind CSS via CDN
- **Authentication**: Django's built-in user system
- **Custom Features**: Template filters for enhanced form styling

## Default Teams

The system comes with 7 pre-configured color teams:
1. Red Team
2. Blue Team  
3. Green Team
4. Yellow Team
5. Orange Team
6. Purple Team
7. Pink Team

## Development

To run the development server:
```bash
py manage.py runserver
```

To create new staff users:
```bash
py manage.py createsuperuser
```

## Security Notes

- Only staff members can access the system
- All score entries are tracked with the user who added them
- Professional login interface with security indicators
- Change the default admin password before production use

## Interface Improvements

The login interface has been completely redesigned with:
- **Gradient Background**: Modern purple-blue gradient with decorative elements
- **Glassmorphism Card**: Semi-transparent login card with backdrop blur
- **Smooth Animations**: Fade-in, float, and shake animations
- **Icon Integration**: User and lock icons in input fields
- **Hover Effects**: Interactive elements with smooth transitions
- **Professional Typography**: Clear hierarchy and modern font styling
- **Mobile Optimization**: Responsive design that works on all screen sizes
