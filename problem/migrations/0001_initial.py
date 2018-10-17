# Generated by Django 2.1.1 on 2018-10-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False, verbose_name='题目编号')),
                ('Headline', models.CharField(max_length=50, verbose_name='题目标题')),
                ('Time_Limit', models.CharField(max_length=30, verbose_name='时间限制')),
                ('Memory_Limit', models.CharField(max_length=30, verbose_name='内存限制')),
                ('Prob_Description', models.TextField(verbose_name='题目描述')),
                ('Input', models.TextField(null=True, verbose_name='输入说明')),
                ('Output', models.TextField(null=True, verbose_name='输出说明')),
                ('Eg_Input', models.TextField(null=True, verbose_name='样例输入')),
                ('Eg_Output', models.TextField(null=True, verbose_name='样例输出')),
                ('Author', models.CharField(max_length=20, null=True, verbose_name='题目作者')),
                ('Up_time', models.DateField(verbose_name='上传时间')),
                ('Total_submision', models.IntegerField(default=0, verbose_name='提交次数')),
                ('Total_AC', models.IntegerField(default=0, verbose_name='AC次数')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('Tag_name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='标签名称')),
                ('Prob_num', models.IntegerField(default=0, verbose_name='标签对应题目数量')),
            ],
        ),
        migrations.AddField(
            model_name='problems',
            name='Tags',
            field=models.ManyToManyField(to='problem.Tag', verbose_name='题目标签'),
        ),
    ]
