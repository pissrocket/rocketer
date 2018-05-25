PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for members
-- ----------------------------
DROP TABLE IF EXISTS "main"."members";
CREATE TABLE "members" (
"userid"  INTEGER NOT NULL,
"coins"  INTEGER NOT NULL DEFAULT 0,
"user_mention"  TEXT,
PRIMARY KEY ("userid" ASC)
);
PRAGMA foreign_keys = ON;
