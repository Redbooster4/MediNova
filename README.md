```mermaid
gantt
    title MediNova Project Execution Timeline
    dateFormat  YYYY-MM-DD
    axisFormat %d %b
    excludes weekends

    %% ========================
    %% PROJECT INITIATION
    %% ========================
    section Initiation & Planning
    Literature Review              :done,    a1, 2026-05-01, 3d
    Requirement Gathering         :done,    a2, after a1, 3d
    Feasibility Study             :done,    a3, after a2, 2d
    Project Approval              :milestone, m1, after a3, 0d

    %% ========================
    %% SYSTEM DESIGN
    %% ========================
    section System Design
    UI/UX Wireframing             :active,  a4, after m1, 4d
    Database Schema Design        :         a5, after a4, 3d
    System Architecture Planning  :         a6, after a5, 3d
    Design Freeze                 :milestone, m2, after a6, 0d

    %% ========================
    %% DEVELOPMENT PHASE
    %% ========================
    section Core Development
    Backend Environment Setup     :         a7, after m2, 3d
    Authentication Module         :         a8, after a7, 4d
    API Development               :         a9, after a8, 5d
    Database Integration          :         a10, after a9, 4d
    Backend Completion            :milestone, m3, after a10, 0d

    section Frontend Development
    UI Implementation             :         a11, after m2, 5d
    Dashboard Development         :         a12, after a11, 5d
    API Integration (Frontend)    :         a13, after a12, 4d
    Frontend Completion           :milestone, m4, after a13, 0d

    %% ========================
    %% TESTING & VALIDATION
    %% ========================
    section Testing Phase
    Unit Testing                  :         a14, after m3, 3d
    Integration Testing           :         a15, after a14, 3d
    System Testing                :         a16, after a15, 3d
    Bug Fixing Cycle              :         a17, after a16, 4d
    Testing Complete              :milestone, m5, after a17, 0d

    %% ========================
    %% DEPLOYMENT & DELIVERY
    %% ========================
    section Deployment & Closure
    Deployment Setup              :         a18, after m5, 2d
    Final Documentation           :         a19, after a18, 3d
    Presentation Preparation      :         a20, after a19, 2d
    Final Submission              :milestone, m6, after a20, 0d
