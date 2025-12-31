-- Challenge 01: Spaghetti → Schema
-- DDL: CREATE TABLE statements
-- 
-- This file defines the target schema for the grocery data.
-- Execute with: psql -f ddl.sql
-- 
-- Schema: grocery
-- Author: [Your Name]
-- Created: [Date]

-- Create schema
CREATE SCHEMA IF NOT EXISTS grocery;

SET search_path TO grocery;

-- ============================================================================
-- DIMENSION TABLES
-- ============================================================================

-- TODO: Add dimension tables after schema design
-- Example:
-- CREATE TABLE dim_date (
--     date_key INTEGER PRIMARY KEY,
--     full_date DATE NOT NULL,
--     year INTEGER NOT NULL,
--     month INTEGER NOT NULL,
--     day INTEGER NOT NULL,
--     day_of_week INTEGER NOT NULL,
--     week_of_year INTEGER NOT NULL,
--     is_weekend BOOLEAN NOT NULL,
--     is_holiday BOOLEAN DEFAULT FALSE
-- );

-- ============================================================================
-- FACT TABLES
-- ============================================================================

-- TODO: Add fact tables after schema design

-- ============================================================================
-- FOREIGN KEY CONSTRAINTS
-- ============================================================================

-- TODO: Add foreign key constraints after tables are created

-- ============================================================================
-- COMMENTS
-- ============================================================================

-- TODO: Add table and column comments for documentation
