resource "google_storage_bucket" "data_bucket" {
  name          = var.bucket_name
  location      = "US"
  force_destroy = true
}

resource "google_storage_bucket_object" "source-videos" {
  for_each = fileset("./", "test-files/source-videos/*" )
  name     = trimprefix(each.value, "test-files/")
  source   = each.value
  bucket   = google_storage_bucket.data_bucket.name
}

# resource "google_storage_bucket_object" "style-images" {
#   for_each = fileset(path.module, "./test-files/style-images/*" )
#   name     = trimprefix(each.value, "test-files/")
#   source   = each.value
#   bucket   = var.bucket_name
# }

