# Generated by Django 2.2.10 on 2020-05-14 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Photo", models.ImageField(default="Icon.jpg", upload_to="managers")),
                ("Age", models.IntegerField()),
                (
                    "user_ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Warehouse",
            fields=[
                ("Item_Group_Code", models.IntegerField()),
                (
                    "Company_Item_code",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("Company_Code", models.IntegerField()),
                ("Quantity", models.IntegerField()),
                ("Name", models.CharField(max_length=100)),
                ("Description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Salesperson",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                (
                    "Photo",
                    models.ImageField(default="Icon.jpg", upload_to="salesperson"),
                ),
                ("Age", models.IntegerField()),
                ("last_location_lat", models.FloatField(null=True)),
                ("last_location_long", models.FloatField(null=True)),
                ("isLoggedin", models.BooleanField(default=False)),
                (
                    "Managed_By",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="salespersonTrackerREST.Manager",
                    ),
                ),
                (
                    "User_ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemAssign",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Assign_Date", models.DateField()),
                ("Assign_Time", models.TimeField()),
                ("assign_quantity", models.IntegerField()),
                (
                    "Assigned_By",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="salespersonTrackerREST.Manager",
                    ),
                ),
                (
                    "Assigned_To",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="salespersonTrackerREST.Salesperson",
                    ),
                ),
                (
                    "Item_Ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Warehouse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Quantity", models.IntegerField(blank=True)),
                (
                    "Salesperson_Ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Salesperson",
                    ),
                ),
                (
                    "item_Ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Warehouse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DailyTarget",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Assigned_Date", models.DateField()),
                ("Assigned_Time", models.TimeField()),
                ("Quantity", models.IntegerField()),
                ("Completed", models.BooleanField()),
                ("Notes", models.TextField()),
                (
                    "Assigned_By",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="salespersonTrackerREST.Manager",
                    ),
                ),
                (
                    "Assigned_To",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Salesperson",
                    ),
                ),
                (
                    "Item_Ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Inventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Issued_To", models.CharField(max_length=100)),
                ("Quantity", models.IntegerField()),
                ("Buyer_Contact", models.IntegerField()),
                ("Buyer_email", models.CharField(max_length=100)),
                ("SoftCopy", models.FileField(upload_to="Bills")),
                (
                    "Salesperson_Ref",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="salespersonTrackerREST.Salesperson",
                    ),
                ),
                (
                    "Target_ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.DailyTarget",
                    ),
                ),
                (
                    "item_ref",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salespersonTrackerREST.Inventory",
                    ),
                ),
            ],
        ),
    ]
