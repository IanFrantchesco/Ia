PRAGMA foreign_keys=OFF;--> statement-breakpoint
CREATE TABLE `articles_new` (
	`doi` text PRIMARY KEY NOT NULL,
	`title` text NOT NULL,
	`title_pt` text DEFAULT '' NOT NULL,
	`description` text DEFAULT '' NOT NULL,
	`summary_pt` text DEFAULT '' NOT NULL,
	`link` text NOT NULL,
	`pub_date` text DEFAULT '' NOT NULL,
	`journal` text NOT NULL CHECK (`journal` IN ('JAMA', 'HR', 'JCE', 'CAH')),
	`created_at` integer NOT NULL
);--> statement-breakpoint
INSERT INTO `articles_new` SELECT * FROM `articles`;--> statement-breakpoint
DROP TABLE `articles`;--> statement-breakpoint
ALTER TABLE `articles_new` RENAME TO `articles`;--> statement-breakpoint
CREATE INDEX `idx_articles_journal` ON `articles` (`journal`);--> statement-breakpoint
CREATE INDEX `idx_articles_created_at` ON `articles` (`created_at`);--> statement-breakpoint
PRAGMA foreign_keys=ON;
