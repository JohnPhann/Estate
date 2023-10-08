# Generated by Django 4.2 on 2023-09-01 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('typeCustomer', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='HomeHire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('maBDS', models.CharField(max_length=50, unique=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m')),
                ('adress', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('ward', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('area', models.IntegerField()),
                ('saleablearea', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('wc', models.IntegerField()),
                ('horizontal', models.IntegerField()),
                ('lagreRoad', models.IntegerField()),
                ('margin', models.IntegerField()),
                ('price', models.IntegerField()),
                ('commission', models.CharField(max_length=150)),
                ('note', models.CharField(max_length=150)),
                ('propose', models.CharField(max_length=150)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.categories')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.customer')),
            ],
            options={
                'db_table': 'homeHire',
            },
        ),
        migrations.CreateModel(
            name='HomeSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('maBDS', models.CharField(max_length=50, unique=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m')),
                ('adress', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('ward', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('area', models.IntegerField()),
                ('saleablearea', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('wc', models.IntegerField()),
                ('horizontal', models.IntegerField()),
                ('lagreRoad', models.IntegerField()),
                ('margin', models.IntegerField()),
                ('price', models.IntegerField()),
                ('commission', models.CharField(max_length=150)),
                ('note', models.CharField(max_length=150)),
                ('propose', models.CharField(max_length=150)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.categories')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.customer')),
            ],
            options={
                'db_table': 'homeSale',
            },
        ),
        migrations.CreateModel(
            name='Orientation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'orientation',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m')),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sale',
            },
        ),
        migrations.CreateModel(
            name='StateHire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'stateHire',
            },
        ),
        migrations.CreateModel(
            name='StateSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'stateSale',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m')),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.role')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('typeHost', models.CharField(max_length=50)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.sale')),
            ],
            options={
                'db_table': 'host',
            },
        ),
        migrations.CreateModel(
            name='homeSaleUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='uploads/%Y/%m')),
                ('homeSale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.homesale')),
            ],
            options={
                'db_table': 'homeSaleUpload',
            },
        ),
        migrations.AddField(
            model_name='homesale',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.host'),
        ),
        migrations.AddField(
            model_name='homesale',
            name='orientation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.orientation'),
        ),
        migrations.AddField(
            model_name='homesale',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.sale'),
        ),
        migrations.AddField(
            model_name='homesale',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.staff'),
        ),
        migrations.AddField(
            model_name='homesale',
            name='stateHire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.statehire'),
        ),
        migrations.AddField(
            model_name='homesale',
            name='stateSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.statesale'),
        ),
        migrations.CreateModel(
            name='homeHireUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='uploads/%Y/%m')),
                ('homeHire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.homehire')),
            ],
            options={
                'db_table': 'homeHireUpload',
            },
        ),
        migrations.AddField(
            model_name='homehire',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.host'),
        ),
        migrations.AddField(
            model_name='homehire',
            name='orientation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.orientation'),
        ),
        migrations.AddField(
            model_name='homehire',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.sale'),
        ),
        migrations.AddField(
            model_name='homehire',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.staff'),
        ),
        migrations.AddField(
            model_name='homehire',
            name='stateHire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.statehire'),
        ),
        migrations.AddField(
            model_name='homehire',
            name='stateSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.statesale'),
        ),
        migrations.AddField(
            model_name='customer',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realEstate.sale'),
        ),
    ]
