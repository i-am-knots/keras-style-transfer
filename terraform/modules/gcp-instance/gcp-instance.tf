resource "google_compute_instance" "gpu_compute_instance" {
  name         = var.instance_name
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "projects/ml-images/global/images/c1-deeplearning-tf-2-1-cu110-v20211022-debian-10"
      #image = "projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20211102"
    }
  }

  // Local SSD disk
  scratch_disk {
    interface = "SCSI"
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  guest_accelerator {
    type  = "nvidia-tesla-k80"
    count = 1
  }

  scheduling {
    preemptible       = true
    automatic_restart = false
  }

  metadata_startup_script = "git clone https://github.com/i-am-knots/keras-style-transfer.git"

  service_account {
    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    email  = "257220959067-compute@developer.gserviceaccount.com" 
    scopes = ["cloud-platform"]
  }
}
