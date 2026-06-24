CREATE TABLE `articles` (
	`doi` text PRIMARY KEY NOT NULL,
	`title` text NOT NULL,
	`title_pt` text DEFAULT '' NOT NULL,
	`description` text DEFAULT '' NOT NULL,
	`summary_pt` text DEFAULT '' NOT NULL,
	`link` text NOT NULL,
	`pub_date` text DEFAULT '' NOT NULL,
	`journal` text NOT NULL,
	`created_at` integer NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_articles_journal` ON `articles` (`journal`);--> statement-breakpoint
CREATE INDEX `idx_articles_created_at` ON `articles` (`created_at`);