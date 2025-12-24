output "cluster_name" {
  value = aws_eks_cluster.this.name
}

output "cluster_endpoint" {
  value = aws_eks_cluster.this.endpoint
}

output "cluster_kubeconfig_certificate_authority" {
  value = aws_eks_cluster.this.certificate_authority[0].data
}

output "node_group_arn" {
  value = aws_eks_node_group.this.arn
}

output "node_role_arn" {
  value = aws_iam_role.eks_node_role.arn
}
