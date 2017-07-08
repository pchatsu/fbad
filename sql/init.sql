DROP TABLE IF EXISTS gd_video;
DROP TABLE IF EXISTS fb_account;
DROP TABLE IF EXISTS gd_video_fb_account_relation;

CREATE TABLE gd_video (
    id VARCHAR(255) PRIMARY KEY NOT NULL
    ,name VARCHAR(255) NOT NULL
    ,created_at INT NOT NULL
);

CREATE TABLE fb_account (
    id BIGINT PRIMARY KEY NOT NULL
    ,created_at INT NOT NULL
);

CREATE TABLE gd_video_fb_account_relation (
    fb_account_id BIGINT NOT NULL
    ,gd_video_id BIGINT NOT NULL
    ,created_at INT NOT NULL
    ,uploaded_at INT NOT NULL DEFAULT 0
    ,PRIMARY KEY(gd_video_id, fb_account_id)
);
CREATE INDEX gd_video_fb_account_relation_i1 ON gd_video_fb_account_relation (fb_account_id, gd_video_id);
