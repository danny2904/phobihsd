# Thesis Workspace Guide

Thư mục này lưu toàn bộ tài liệu phục vụ viết luận án `phobihsd`.

## Cấu trúc chuẩn

- [thesis_phobihsd.md](/home/ubuntu/project/phobihsd/docs/thesis/thesis_phobihsd.md): bản thảo luận án dạng Markdown.
- [thesis_phobihsd.pdf](/home/ubuntu/project/phobihsd/docs/thesis/thesis_phobihsd.pdf): bản PDF nguồn.
- [references/](/home/ubuntu/project/phobihsd/docs/thesis/references): toàn bộ danh mục tài liệu tham khảo theo chương.
- [zotero/ris/](/home/ubuntu/project/phobihsd/docs/thesis/zotero/ris): các file RIS dùng để sync vào Zotero.
- [zotero/tests/](/home/ubuntu/project/phobihsd/docs/thesis/zotero/tests): file Word test cho pipeline cite động.

## Quy tắc map cite số

- Dùng duy nhất file master map:
  - [references_master_map.md](/home/ubuntu/project/phobihsd/docs/thesis/references/references_master_map.md)
- Cấu trúc map chuẩn: `[n] -> canonical -> DOI -> Zotero key`.
- Khi có trùng tài liệu (cùng DOI), luôn cite theo `canonical` để tránh tạo trùng trong Word/Zotero.
- Nếu bản Word đang lệch số tham khảo (ví dụ còn `[80]` nhưng danh mục chuẩn chỉ còn đến `[79]`):
  - bật rule shift fallback trong skill để map `[n] -> [n-1]` ở vùng lệch,
  - nhưng vẫn giữ nguyên số hiển thị trong nội dung luận án.

## Workflow Zotero đề xuất

1. Sync RIS vào collection `phobihsd` bằng script skill.
2. Chạy repair metadata để bổ sung đủ field từ Crossref.
3. Dùng master map để convert cite số `[n]` trong `.docx` thành Zotero dynamic field.
4. Mở Word và bấm Zotero `Refresh` để cập nhật citation/bibliography.

## Lưu ý quan trọng

- Không chỉnh tay mã `{ ADDIN ZOTERO_ITEM ... }` trong Word.
- Không tạo nhiều map rời cho cùng một tập tài liệu; luôn cập nhật vào `references_master_map.md`.
- Trước khi viết chương mới, kiểm tra trùng DOI để tránh sinh số tham khảo mới cho cùng một tài liệu.
