# Installation Guide

## Prerequisites

- Python 3.6 or higher
- Docker Engine
- Web server (Apache/Nginx) with CGI support
- Camera and microphone for authentication
- Git

## Step-by-Step Installation

### 1. System Setup

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3 python3-pip docker.io apache2 libapache2-mod-python
sudo systemctl enable docker
sudo systemctl start docker
```

#### CentOS/RHEL
```bash
sudo yum install python3 python3-pip docker httpd mod_python
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl enable httpd
sudo systemctl start httpd
```

### 2. Python Dependencies

```bash
cd cloud-platform
pip3 install -r requirements.txt
```

### 3. Web Server Configuration

#### Apache CGI Setup
```apache
# Add to /etc/apache2/sites-available/000-default.conf
<Directory "/var/www/html/cloud-platform/backend-services">
    Options +ExecCGI
    AddHandler cgi-script .py
    Require all granted
</Directory>
```

```bash
sudo a2enmod cgi
sudo systemctl restart apache2
```

### 4. Docker Configuration

```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Test Docker installation
docker --version
docker run hello-world
```

### 5. File Permissions

```bash
chmod +x backend-services/*.py
chmod -R 755 web-interface/
chmod -R 755 ai-authentication/
```

### 6. Configuration Updates

1. Update server IP addresses in HTML files:
   - `web-interface/index.html`
   - `web-interface/docker.html`
   - All service pages

2. Configure Docker host in `backend-services/dockerlistv2.py`

3. Set up authentication credentials in AI notebooks

### 7. Testing the Installation

1. **Web Interface**: Access `http://localhost/cloud-platform/web-interface/`
2. **AI Authentication**: Run Jupyter notebooks in `ai-authentication/`
3. **Backend Services**: Test CGI scripts through web interface

## Troubleshooting

### Common Issues

1. **CGI Scripts Not Working**
   - Check Apache error logs: `tail -f /var/log/apache2/error.log`
   - Verify file permissions
   - Ensure Python path is correct in scripts

2. **Docker Connection Issues**
   - Verify Docker daemon is running
   - Check SSH key setup for remote Docker management
   - Test Docker commands manually

3. **Face Recognition Errors**
   - Install OpenCV with GUI support: `pip install opencv-python-headless`
   - Check camera permissions
   - Verify cascade file path

4. **Speech Recognition Problems**
   - Test microphone: `arecord -l`
   - Check internet connection for Google Speech API
   - Verify audio input device

### Log Locations

- Apache logs: `/var/log/apache2/`
- Docker logs: `docker logs <container>`
- Application logs: Check individual service logs

## Security Considerations

1. Change default passwords and authentication credentials
2. Use HTTPS in production
3. Implement firewall rules
4. Regular security updates
5. Monitor access logs

## Performance Optimization

1. Enable Apache caching modules
2. Optimize Docker resource limits
3. Use CDN for static assets
4. Implement database indexing for large datasets

## Backup and Recovery

1. Regular backups of configuration files
2. Docker volume backups
3. Database exports
4. System state snapshots

## Support

For installation issues:
1. Check system logs
2. Verify all prerequisites
3. Review configuration files
4. Consult troubleshooting section
5. Create GitHub issue with detailed error information
