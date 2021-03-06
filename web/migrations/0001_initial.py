# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-08 08:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('name', models.CharField(max_length=32)),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='备注')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now, help_text='yyyy-mm-dd HH:MM:SS')),
                ('valid_end_time', models.DateTimeField(blank=True, help_text='yyyy-mm-dd HH:MM:SS', null=True)),
            ],
            options={
                'verbose_name': 'CrazyEye账户',
                'verbose_name_plural': 'CrazyEye账户',
                'permissions': (('web_access_dashboard', '可以访问 审计主页'), ('web_batch_cmd_exec', '可以访问 批量命令执行页面'), ('web_batch_batch_file_transfer', '可以访问 批量文件分发页面'), ('web_config_center', '可以访问 堡垒机配置中心'), ('web_config_items', '可以访问 堡垒机各配置列表'), ('web_invoke_admin_action', '可以进行admin action执行动作'), ('web_table_change_page', '可以访问 堡垒机各配置项修改页'), ('web_table_change', '可以修改 堡垒机各配置项')),
            },
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.IntegerField(choices=[(0, 'CMD'), (1, 'Login'), (2, 'Logout'), (3, 'GetFile'), (4, 'SendFile'), (5, 'exception')], default=0)),
                ('cmd', models.TextField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '审计日志old',
                'verbose_name_plural': '审计日志old',
            },
        ),
        migrations.CreateModel(
            name='BindHosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '主机与远程用户绑定',
                'verbose_name_plural': '主机远程与用户绑定',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='HostGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
                ('bind_hosts', models.ManyToManyField(blank=True, to='web.BindHosts')),
            ],
            options={
                'verbose_name': '主机组',
                'verbose_name_plural': '主机组',
            },
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('system_type', models.CharField(choices=[('windows', 'Windows'), ('linux', 'Linux/Unix')], default='linux', max_length=32)),
                ('port', models.IntegerField(default=22)),
                ('enabled', models.BooleanField(default=True, help_text='主机若不想被用户访问可以去掉此选项')),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='HostUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_method', models.CharField(choices=[('ssh-password', 'SSH/ Password'), ('ssh-key', 'SSH/KEY')], help_text='如果选择SSH/KEY，请确保你的私钥文件已在settings.py中指定', max_length=16)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(blank=True, help_text='如果auth_method选择的是SSH/KEY,那此处不需要填写..', max_length=64, null=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': '远程用户',
                'verbose_name_plural': '远程用户',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='n/a', max_length=128)),
                ('closed', models.BooleanField(default=False)),
                ('cmd_count', models.IntegerField(default=0)),
                ('stay_time', models.IntegerField(default=0, help_text='每次刷新自动计算停留时间', verbose_name='停留时长(seconds)')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bind_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHosts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '审计日志',
                'verbose_name_plural': '审计日志',
            },
        ),
        migrations.CreateModel(
            name='SessionTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('task_type', models.CharField(choices=[('cmd', 'CMD'), ('file_send', '批量发送文件'), ('file_get', '批量下载文件')], max_length=50)),
                ('files_dir', models.CharField(blank=True, max_length=32, null=True, verbose_name='文件上传临时目录')),
                ('cmd', models.TextField()),
                ('expire_time', models.IntegerField(default=30)),
                ('task_pid', models.IntegerField(default=0)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('hosts', models.ManyToManyField(to='web.BindHosts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '批量任务',
                'verbose_name_plural': '批量任务',
            },
        ),
        migrations.CreateModel(
            name='TaskLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event_log', models.TextField()),
                ('result', models.CharField(choices=[('success', 'Success'), ('failed', 'Failed'), ('unknown', 'Unknown')], default='unknown', max_length=30)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('bind_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHosts')),
                ('child_of_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.TaskLog')),
            ],
            options={
                'verbose_name': '批量任务日志',
                'verbose_name_plural': '批量任务日志',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire', models.IntegerField(default=300)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHosts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hostusers',
            unique_together=set([('auth_method', 'password', 'username')]),
        ),
        migrations.AddField(
            model_name='hosts',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.IDC'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Hosts'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.HostUsers', verbose_name='远程用户'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHosts'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SessionTrack'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bind_hosts',
            field=models.ManyToManyField(blank=True, to='web.BindHosts', verbose_name='授权主机'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Department', verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='host_groups',
            field=models.ManyToManyField(blank=True, to='web.HostGroups', verbose_name='授权主机组'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosts',
            unique_together=set([('host', 'host_user')]),
        ),
    ]
