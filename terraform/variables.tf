variable "region" {
  type    = string
  default = "eu-west-3"
}

variable "cluster_name" {
  type    = string
  default = "devops-assessment"
}

variable "node_group_name" {
  type    = string
  default = "linux-nodes"
}

variable "desired_capacity" {
  type    = number
  default = 2
}

variable "max_capacity" {
  type    = number
  default = 2
}

variable "min_capacity" {
  type    = number
  default = 2
}

variable "node_instance_type" {
  type    = string
  default = "t3.micro" # Free Tier compatible
}
