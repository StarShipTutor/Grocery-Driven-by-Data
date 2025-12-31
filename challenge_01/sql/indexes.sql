-- Challenge 01: Spaghetti → Schema
-- Indexes for query optimization
-- 
-- Execute AFTER ddl.sql and initial data load
-- Execute with: psql -f indexes.sql

SET search_path TO grocery;

-- ============================================================================
-- PRIMARY KEY INDEXES (created automatically)
-- ============================================================================

-- ============================================================================
-- FOREIGN KEY INDEXES
-- ============================================================================

-- TODO: Add indexes on foreign key columns
-- Example:
-- CREATE INDEX idx_sales_product_id ON fact_sales(product_id);
-- CREATE INDEX idx_sales_store_id ON fact_sales(store_id);
-- CREATE INDEX idx_sales_date_key ON fact_sales(date_key);

-- ============================================================================
-- QUERY OPTIMIZATION INDEXES
-- ============================================================================

-- TODO: Add indexes based on common query patterns
-- Example:
-- CREATE INDEX idx_sales_date_store ON fact_sales(date_key, store_id);

-- ============================================================================
-- PARTIAL INDEXES
-- ============================================================================

-- TODO: Add partial indexes for filtered queries
-- Example:
-- CREATE INDEX idx_sales_promo ON fact_sales(promotion_id) 
--     WHERE promotion_id IS NOT NULL;

-- ============================================================================
-- ANALYZE TABLES
-- ============================================================================

-- TODO: Add ANALYZE statements after data load
-- ANALYZE fact_sales;
