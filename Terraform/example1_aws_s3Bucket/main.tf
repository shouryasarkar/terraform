resource "aws_s3_bucket" "supatra" {
  count = 2
  bucket = "my-tf-test-bucket-supatra2-${count.index}"

  tags = {
    Name        = "Supatra bucket"
    Environment = "Developer"
  }
}
