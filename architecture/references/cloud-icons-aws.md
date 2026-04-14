### 6.1 AWS Icons (`mxgraph.aws4.*`)

AWS icons use the `mxgraph.aws4` namespace. Each service category has a corresponding official brand color.

#### Compute — `fillColor=#ED7100`

| Service | Style String | Description |
|------|-----------|------|
| EC2 | `shape=mxgraph.aws4.ec2;fillColor=#ED7100;strokeColor=#ffffff;` | Elastic compute instances |
| Lambda | `shape=mxgraph.aws4.lambda_function;fillColor=#ED7100;strokeColor=#ffffff;` | Serverless functions |
| ECS | `shape=mxgraph.aws4.ecs;fillColor=#ED7100;strokeColor=#ffffff;` | Container service |
| EKS | `shape=mxgraph.aws4.eks;fillColor=#ED7100;strokeColor=#ffffff;` | Kubernetes service |
| Fargate | `shape=mxgraph.aws4.fargate;fillColor=#ED7100;strokeColor=#ffffff;` | Serverless containers |
| Auto Scaling | `shape=mxgraph.aws4.auto_scaling2;fillColor=#ED7100;strokeColor=#ffffff;` | Auto scaling |
| Elastic Beanstalk | `shape=mxgraph.aws4.elastic_beanstalk;fillColor=#ED7100;strokeColor=#ffffff;` | Application deployment platform |

#### Storage — `fillColor=#3F8624`

| Service | Style String | Description |
|------|-----------|------|
| S3 | `shape=mxgraph.aws4.s3;fillColor=#3F8624;strokeColor=#ffffff;` | Object storage |
| EBS | `shape=mxgraph.aws4.elastic_block_store;fillColor=#3F8624;strokeColor=#ffffff;` | Block storage |
| EFS | `shape=mxgraph.aws4.elastic_file_system;fillColor=#3F8624;strokeColor=#ffffff;` | File storage |
| S3 Glacier | `shape=mxgraph.aws4.glacier;fillColor=#3F8624;strokeColor=#ffffff;` | Archive storage |

#### Database — `fillColor=#C925D1`

| Service | Style String | Description |
|------|-----------|------|
| RDS | `shape=mxgraph.aws4.rds;fillColor=#C925D1;strokeColor=#ffffff;` | Relational database |
| DynamoDB | `shape=mxgraph.aws4.dynamodb;fillColor=#C925D1;strokeColor=#ffffff;` | NoSQL database |
| ElastiCache | `shape=mxgraph.aws4.elasticache;fillColor=#C925D1;strokeColor=#ffffff;` | Cache service |
| Aurora | `shape=mxgraph.aws4.aurora;fillColor=#C925D1;strokeColor=#ffffff;` | High-performance relational database |
| Redshift | `shape=mxgraph.aws4.redshift;fillColor=#C925D1;strokeColor=#ffffff;` | Data warehouse |

#### Networking — `fillColor=#8C4FFF`

| Service | Style String | Description |
|------|-----------|------|
| VPC | `shape=mxgraph.aws4.vpc;fillColor=#8C4FFF;strokeColor=#ffffff;` | Virtual private cloud |
| CloudFront | `shape=mxgraph.aws4.cloudfront;fillColor=#8C4FFF;strokeColor=#ffffff;` | CDN content delivery |
| Route 53 | `shape=mxgraph.aws4.route_53;fillColor=#8C4FFF;strokeColor=#ffffff;` | DNS service |
| API Gateway | `shape=mxgraph.aws4.api_gateway;fillColor=#8C4FFF;strokeColor=#ffffff;` | API gateway |
| ELB | `shape=mxgraph.aws4.elastic_load_balancing;fillColor=#8C4FFF;strokeColor=#ffffff;` | Load balancer |
| ALB | `shape=mxgraph.aws4.application_load_balancer;fillColor=#8C4FFF;strokeColor=#ffffff;` | Application load balancer |
| NLB | `shape=mxgraph.aws4.network_load_balancer;fillColor=#8C4FFF;strokeColor=#ffffff;` | Network load balancer |

#### Security — `fillColor=#DD344C`

| Service | Style String | Description |
|------|-----------|------|
| IAM | `shape=mxgraph.aws4.iam;fillColor=#DD344C;strokeColor=#ffffff;` | Identity and access management |
| Cognito | `shape=mxgraph.aws4.cognito;fillColor=#DD344C;strokeColor=#ffffff;` | User authentication |
| WAF | `shape=mxgraph.aws4.waf;fillColor=#DD344C;strokeColor=#ffffff;` | Web application firewall |
| Shield | `shape=mxgraph.aws4.shield;fillColor=#DD344C;strokeColor=#ffffff;` | DDoS protection |
| KMS | `shape=mxgraph.aws4.key_management_service;fillColor=#DD344C;strokeColor=#ffffff;` | Key management |
| Secrets Manager | `shape=mxgraph.aws4.secrets_manager;fillColor=#DD344C;strokeColor=#ffffff;` | Secrets management |

#### Application Integration — `fillColor=#E7157B`

| Service | Style String | Description |
|------|-----------|------|
| SQS | `shape=mxgraph.aws4.sqs;fillColor=#E7157B;strokeColor=#ffffff;` | Message queue |
| SNS | `shape=mxgraph.aws4.sns;fillColor=#E7157B;strokeColor=#ffffff;` | Notification service |
| Step Functions | `shape=mxgraph.aws4.step_functions;fillColor=#E7157B;strokeColor=#ffffff;` | Workflow orchestration |
| EventBridge | `shape=mxgraph.aws4.eventbridge;fillColor=#E7157B;strokeColor=#ffffff;` | Event bus |

#### Management & Monitoring — `fillColor=#E7157B`

| Service | Style String | Description |
|------|-----------|------|
| CloudWatch | `shape=mxgraph.aws4.cloudwatch;fillColor=#E7157B;strokeColor=#ffffff;` | Monitoring service |
| CloudFormation | `shape=mxgraph.aws4.cloudformation;fillColor=#E7157B;strokeColor=#ffffff;` | Infrastructure as code |

#### AI / ML — `fillColor=#01A88D`

> **IMPORTANT**: Bedrock, SageMaker, OpenSearch and other AI/ML services use the `resourceIcon` + `resIcon` two-part style. The `shape=mxgraph.aws4.resourceIcon` sets the icon container, and `resIcon=mxgraph.aws4.{service}` specifies the actual service icon.

| Service | Style String | Description |
|------|-----------|------|
| Bedrock | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;fillColor=#01A88D;strokeColor=#ffffff;` | Foundation model service |
| Bedrock Knowledge Bases | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;fillColor=#01A88D;strokeColor=#ffffff;` | RAG knowledge base (use Bedrock icon) |
| SageMaker | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sagemaker;fillColor=#01A88D;strokeColor=#ffffff;` | ML platform |
| OpenSearch Service | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticsearch_service;fillColor=#01A88D;strokeColor=#ffffff;` | Search & vector database |
| Comprehend | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.comprehend;fillColor=#01A88D;strokeColor=#ffffff;` | NLP service |
| Rekognition | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rekognition;fillColor=#01A88D;strokeColor=#ffffff;` | Image/video analysis |
| Textract | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;fillColor=#01A88D;strokeColor=#ffffff;` | Document text extraction |
| Kendra | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kendra;fillColor=#01A88D;strokeColor=#ffffff;` | Intelligent search |
| Lex | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lex;fillColor=#01A88D;strokeColor=#ffffff;` | Conversational AI |
| Polly | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.polly;fillColor=#01A88D;strokeColor=#ffffff;` | Text-to-speech |
| Transcribe | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transcribe;fillColor=#01A88D;strokeColor=#ffffff;` | Speech-to-text |
| Translate | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.translate;fillColor=#01A88D;strokeColor=#ffffff;` | Language translation |

**Full style string for AI/ML icons (copy-paste template):**

```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;whiteSpace=wrap;html=1;fillColor=#01A88D;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;
```



### 6.4 AWS Service Category Color Quick Reference

AWS service categories use different official brand colors for quick visual distinction of service types in architecture diagrams:

| Service Category | fillColor | Color Description |
|----------|-----------|----------|
| Compute | `#ED7100` | Orange |
| Storage | `#3F8624` | Green |
| Database | `#C925D1` | Purple |
| Networking | `#8C4FFF` | Blue-purple |
| Security | `#DD344C` | Red |
| Application Integration | `#E7157B` | Pink |
| AI / ML | `#01A88D` | Teal |

### 6.5 Cloud Icon Usage Example

The following example demonstrates how to use cloud icons in architecture diagrams:

```xml
<mxCell id="aws-alb" value="ALB" 
        style="shape=mxgraph.aws4.application_load_balancer;whiteSpace=wrap;html=1;fillColor=#8C4FFF;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="60" height="60" as="geometry"/>
</mxCell>
<mxCell id="aws-ec2" value="Web Server" 
        style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#ED7100;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="300" y="200" width="60" height="60" as="geometry"/>
</mxCell>
<mxCell id="aws-rds" value="MySQL" 
        style="shape=mxgraph.aws4.rds;whiteSpace=wrap;html=1;fillColor=#C925D1;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="500" y="200" width="60" height="60" as="geometry"/>
</mxCell>
```

