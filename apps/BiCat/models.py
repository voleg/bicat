# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Inv(models.Model):
    inv_id = models.AutoField(primary_key=True, db_column='INV_ID') # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    t990t = models.CharField(max_length=255, db_column='T990t', blank=True) # Field name made lowercase.
    t090h = models.CharField(max_length=255, db_column='T090h', blank=True) # Field name made lowercase.
    t090e = models.CharField(max_length=255, db_column='T090e', blank=True) # Field name made lowercase.
    t090f = models.CharField(max_length=255, db_column='T090f', blank=True) # Field name made lowercase.
    t090w = models.CharField(max_length=255, db_column='T090w', blank=True) # Field name made lowercase.
    t876c = models.CharField(max_length=255, db_column='T876c', blank=True) # Field name made lowercase.
    t876p = models.CharField(max_length=255, db_column='T876p', blank=True) # Field name made lowercase.
    t020d = models.CharField(max_length=255, db_column='T020d', blank=True) # Field name made lowercase.
    t020e = models.CharField(max_length=255, db_column='T020e', blank=True) # Field name made lowercase.
    t990n = models.CharField(max_length=255, db_column='T990n', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    regdate = models.FloatField(null=True, db_column='REGDATE', blank=True) # Field name made lowercase.
    invmode = models.CharField(max_length=1, db_column='INVMODE', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    custom4 = models.CharField(max_length=255, db_column='CUSTOM4', blank=True) # Field name made lowercase.
    custom5 = models.CharField(max_length=255, db_column='CUSTOM5', blank=True) # Field name made lowercase.
    def __unicode__(self):
        return str(self.inv_id) + ":" + str(self.t090e)
    class Meta:
        db_table = u'INV'

class Invoff(models.Model):
    inv_id = models.IntegerField(primary_key=True, db_column='INV_ID') # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    t990t = models.CharField(max_length=255, db_column='T990t', blank=True) # Field name made lowercase.
    t090h = models.CharField(max_length=255, db_column='T090h', blank=True) # Field name made lowercase.
    t090e = models.CharField(max_length=255, db_column='T090e', blank=True) # Field name made lowercase.
    t090f = models.CharField(max_length=255, db_column='T090f', blank=True) # Field name made lowercase.
    t090w = models.CharField(max_length=255, db_column='T090w', blank=True) # Field name made lowercase.
    t876c = models.CharField(max_length=255, db_column='T876c', blank=True) # Field name made lowercase.
    t876p = models.CharField(max_length=255, db_column='T876p', blank=True) # Field name made lowercase.
    t020d = models.CharField(max_length=255, db_column='T020d', blank=True) # Field name made lowercase.
    t020e = models.CharField(max_length=255, db_column='T020e', blank=True) # Field name made lowercase.
    t990n = models.CharField(max_length=255, db_column='T990n', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    offdate = models.FloatField(null=True, db_column='OFFDATE', blank=True) # Field name made lowercase.
    invmode = models.CharField(max_length=1, db_column='INVMODE', blank=True) # Field name made lowercase.
    notes = models.CharField(max_length=255, db_column='NOTES', blank=True) # Field name made lowercase.
    wroffact = models.CharField(max_length=255, db_column='WROFFACT', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    custom4 = models.CharField(max_length=255, db_column='CUSTOM4', blank=True) # Field name made lowercase.
    custom5 = models.CharField(max_length=255, db_column='CUSTOM5', blank=True) # Field name made lowercase.
    def __unicode__(self):
        return str(self.t090e) + " " + self.notes
    class Meta:
        db_table = u'INVOFF'

class Marcstat(models.Model):
    stat_id = models.AutoField(primary_key=True, db_column='STAT_ID') # Field name made lowercase.
    username = models.CharField(max_length=32, db_column='USERNAME', blank=True) # Field name made lowercase.
    opcode = models.IntegerField(null=True, db_column='OPCODE', blank=True) # Field name made lowercase.
    datestat = models.FloatField(null=True, db_column='DATESTAT', blank=True) # Field name made lowercase.
    str1 = models.CharField(max_length=255, db_column='STR1', blank=True) # Field name made lowercase.
    str2 = models.CharField(max_length=255, db_column='STR2', blank=True) # Field name made lowercase.
    str3 = models.CharField(max_length=255, db_column='STR3', blank=True) # Field name made lowercase.
    int1 = models.IntegerField(null=True, db_column='INT1', blank=True) # Field name made lowercase.
    int2 = models.IntegerField(null=True, db_column='INT2', blank=True) # Field name made lowercase.
    int3 = models.IntegerField(null=True, db_column='INT3', blank=True) # Field name made lowercase.
    date1 = models.FloatField(null=True, db_column='DATE1', blank=True) # Field name made lowercase.
    date2 = models.FloatField(null=True, db_column='DATE2', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MARCSTAT'

class Metaidx(models.Model):
    name = models.CharField(max_length=32, primary_key=True, db_column='NAME') # Field name made lowercase.
    type = models.CharField(max_length=32, db_column='TYPE') # Field name made lowercase.
    maxlen = models.IntegerField(null=True, db_column='MAXLEN', blank=True) # Field name made lowercase.
    tags = models.CharField(max_length=40, db_column='TAGS', blank=True) # Field name made lowercase.
    caption = models.CharField(max_length=50, db_column='CAPTION', blank=True) # Field name made lowercase.
    sep = models.CharField(max_length=64, db_column='SEP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'METAIDX'

class Mobject(models.Model):
    name = models.CharField(max_length=255, primary_key=True, db_column='NAME') # Field name made lowercase.
    typ = models.CharField(max_length=64, db_column='TYP') # Field name made lowercase.
    siz = models.IntegerField(null=True, db_column='SIZ', blank=True) # Field name made lowercase.
    crdate = models.FloatField(null=True, db_column='CRDATE', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'MOBJECT'

class Acqu(models.Model):
    acq_id = models.AutoField(primary_key=True, db_column='ACQ_ID') # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    src_id = models.IntegerField(null=True, db_column='SRC_ID', blank=True) # Field name made lowercase.
    ordered = models.IntegerField(null=True, db_column='ORDERED', blank=True) # Field name made lowercase.
    acquired = models.IntegerField(null=True, db_column='ACQUIRED', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    acqdate = models.FloatField(null=True, db_column='ACQDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQU'

class Plant(models.Model):
    plant_id = models.IntegerField(primary_key=True, db_column='PLANT_ID') # Field name made lowercase.
    root_id = models.IntegerField(null=True, db_column='ROOT_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    subrdn = models.CharField(max_length=250, db_column='SUBRDN', blank=True) # Field name made lowercase.
    branch = models.CharField(max_length=250, db_column='BRANCH', blank=True) # Field name made lowercase.
    region = models.CharField(max_length=250, db_column='REGION', blank=True) # Field name made lowercase.
    pstidx = models.CharField(max_length=50, db_column='PSTIDX', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=250, db_column='CITY', blank=True) # Field name made lowercase.
    adrp = models.CharField(max_length=250, db_column='ADRP', blank=True) # Field name made lowercase.
    phcode = models.CharField(max_length=50, db_column='PHCODE', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=250, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=250, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=250, db_column='CHIEF', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PLANT'

class Idx245A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID',) # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX245a'

class Readers(models.Model):
    rdr_id = models.CharField(max_length=16, primary_key=True, db_column='RDR_ID') # Field name made lowercase.
    code = models.CharField(max_length=255, db_column='CODE', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    birthday = models.FloatField(null=True, db_column='BIRTHDAY', blank=True) # Field name made lowercase.
    passport = models.CharField(max_length=255, db_column='PASSPORT', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=255, db_column='ADDRESS', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255, db_column='EMAIL', blank=True) # Field name made lowercase.
    homephone = models.CharField(max_length=255, db_column='HOMEPHONE', blank=True) # Field name made lowercase.
    workphone = models.CharField(max_length=255, db_column='WORKPHONE', blank=True) # Field name made lowercase.
    pager = models.CharField(max_length=255, db_column='PAGER', blank=True) # Field name made lowercase.
    employment = models.CharField(max_length=255, db_column='EMPLOYMENT', blank=True) # Field name made lowercase.
    course = models.CharField(max_length=255, db_column='COURSE', blank=True) # Field name made lowercase.
    profession = models.CharField(max_length=255, db_column='PROFESSION', blank=True) # Field name made lowercase.
    post = models.CharField(max_length=255, db_column='POST', blank=True) # Field name made lowercase.
    regdate = models.FloatField(null=True, db_column='REGDATE', blank=True) # Field name made lowercase.
    reregdate = models.FloatField(null=True, db_column='REREGDATE', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True) # Field name made lowercase.
    photofile = models.CharField(max_length=255, db_column='PHOTOFILE', blank=True) # Field name made lowercase.
    photo = models.TextField(db_column='PHOTO', blank=True) # Field name made lowercase. This field type is a guess.
    sex = models.CharField(max_length=1, db_column='SEX', blank=True) # Field name made lowercase.
    siglas = models.CharField(max_length=255, db_column='SIGLAS', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    custom4 = models.CharField(max_length=255, db_column='CUSTOM4', blank=True) # Field name made lowercase.
    custom5 = models.CharField(max_length=255, db_column='CUSTOM5', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'READERS'

class Siglas(models.Model):
#    id = models.IntegerField(null=True, db_column='ID', blank=True) # Field name made lowercase.
    fullname = models.CharField(max_length=255, db_column='FULLNAME', blank=True) # Field name made lowercase.
    shortname = models.CharField(max_length=255, db_column='SHORTNAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SIGLAS'

class Source(models.Model):
    src_id = models.AutoField(primary_key=True, db_column='SRC_ID') # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SOURCE'

class Dtproperties(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    property = models.TextField() #primary_key=True)
    value = models.TextField(blank=True)
    uvalue = models.CharField(max_length=255, blank=True)
    lvalue = models.TextField(blank=True) # This field type is a guess.
    version = models.IntegerField()
    class Meta:
        db_table = u'dtproperties'

class Dep(models.Model):
    dep_id = models.IntegerField(primary_key=True, db_column='DEP_ID') # Field name made lowercase.
    plant = models.ForeignKey(Plant, null=True, db_column='PLANT_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=250, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=250, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=250, db_column='CHIEF', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DEP'

class Chair(models.Model):
    chair_id = models.IntegerField(primary_key=True, db_column='CHAIR_ID') # Field name made lowercase.
    dep = models.ForeignKey(Dep, null=True, db_column='DEP_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=250, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=250, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=250, db_column='CHIEF', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CHAIR'

class Spec(models.Model):
    spec_id = models.IntegerField(primary_key=True, db_column='SPEC_ID') # Field name made lowercase.
    chair = models.ForeignKey(Chair, null=True, db_column='CHAIR_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    cypher = models.IntegerField(null=True, db_column='CYPHER', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=250, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=250, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=250, db_column='CHIEF', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SPEC'

class Staff(models.Model):
    login = models.CharField(max_length=32, primary_key=True, db_column='LOGIN') # Field name made lowercase.
    password = models.CharField(max_length=32, db_column='PASSWORD', blank=True) # Field name made lowercase.
    grp = models.IntegerField(null=True, db_column='GRP', blank=True) # Field name made lowercase.
    acc = models.IntegerField(null=True, db_column='ACC', blank=True) # Field name made lowercase.
    acc2 = models.IntegerField(null=True, db_column='ACC2', blank=True) # Field name made lowercase.
    phase = models.IntegerField(null=True, db_column='PHASE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'STAFF'

class Tag(models.Model):
    tag = models.CharField(max_length=3, primary_key=True, db_column='TAG') # Field name made lowercase.
    subtag = models.CharField(max_length=1, unique=True, db_column='SUBTAG') # Field name made lowercase.
    flags = models.IntegerField(null=True, db_column='FLAGS', blank=True) # Field name made lowercase.
    separator = models.CharField(max_length=1, db_column='SEPARATOR', blank=True) # Field name made lowercase.
    caption = models.CharField(max_length=40, db_column='CAPTION', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TAG'

class Orders(models.Model):
    rdr_id = models.ForeignKey("Readers", max_length=16, db_column='RDR_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    sigla = models.CharField(max_length=255, db_column='SIGLA', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ORDERS'

class Acqugot(models.Model):
    got_id = models.IntegerField(primary_key=True, db_column='GOT_ID') # Field name made lowercase.
    ord_id = models.IntegerField(null=True, db_column='ORD_ID', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    gotdate = models.FloatField(null=True, db_column='GOTDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQUGOT'

class Acquord(models.Model):
    ord_id = models.IntegerField(primary_key=True, db_column='ORD_ID') # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    src = models.CharField(max_length=255, db_column='SRC', blank=True) # Field name made lowercase.
    publ = models.CharField(max_length=255, db_column='PUBL', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    price = models.IntegerField(null=True, db_column='PRICE', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    getdate = models.FloatField(null=True, db_column='GETDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQUORD'

class Grp(models.Model):
    grp_id = models.IntegerField(primary_key=True, db_column='GRP_ID') # Field name made lowercase.
    spec = models.ForeignKey(Spec, null=True, db_column='SPEC_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=250, db_column='CHIEF', blank=True) # Field name made lowercase.
    educform = models.IntegerField(null=True, db_column='EDUCFORM', blank=True) # Field name made lowercase.
    course = models.IntegerField(null=True, db_column='COURSE', blank=True) # Field name made lowercase.
    semstr = models.IntegerField(null=True, db_column='SEMSTR', blank=True) # Field name made lowercase.
    quantity = models.IntegerField(null=True, db_column='QUANTITY', blank=True) # Field name made lowercase.
    typegrp = models.IntegerField(null=True, db_column='TYPEGRP', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'GRP'

class Discp(models.Model):
    discp_id = models.IntegerField(primary_key=True, db_column='DISCP_ID') # Field name made lowercase.
    chair = models.ForeignKey(Chair, null=True, db_column='CHAIR_ID', blank=True) # Field name made lowercase.
    cypher = models.IntegerField(null=True, db_column='CYPHER', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=250, db_column='NAME', blank=True) # Field name made lowercase.
    spcph_id = models.IntegerField(null=True, db_column='SPCPH_ID', blank=True) # Field name made lowercase.
    drct_id = models.IntegerField(null=True, db_column='DRCT_ID', blank=True) # Field name made lowercase.
    cycl_id = models.IntegerField(null=True, db_column='CYCL_ID', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DISCP'

class Discpx(models.Model):
    discp = models.ForeignKey(Discp, null=True, db_column='DISCP_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    sign = models.IntegerField(null=True, db_column='SIGN', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DISCPX'

class Timetable(models.Model):
    grp = models.ForeignKey(Grp, null=True, db_column='GRP_ID', blank=True) # Field name made lowercase.
    period = models.IntegerField(null=True, db_column='PERIOD', blank=True) # Field name made lowercase.
    discp = models.ForeignKey(Discp, null=True, db_column='DISCP_ID', blank=True) # Field name made lowercase.
    teacher = models.CharField(max_length=250, db_column='TEACHER', blank=True) # Field name made lowercase.
    room = models.CharField(max_length=250, db_column='ROOM', blank=True) # Field name made lowercase.
    day = models.IntegerField(null=True, db_column='DAY', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TIMETABLE'

class Acqusrc(models.Model):
    item = models.CharField(max_length=255, primary_key=True, db_column='ITEM') # Field name made lowercase.
    class Meta:
        db_table = u'ACQUSRC'

class Dbres(models.Model):
    name = models.CharField(max_length=16, primary_key=True, db_column='NAME') # Field name made lowercase.
    ires = models.IntegerField(null=True, db_column='IRES', blank=True) # Field name made lowercase.
    tres = models.CharField(max_length=255, db_column='TRES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DBRES'

class Doc(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    rectype = models.CharField(max_length=1, db_column='RECTYPE', blank=True) # Field name made lowercase.
    biblevel = models.CharField(max_length=1, db_column='BIBLEVEL', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase.
    def __unicode__(self):
        return str(self.doc_id) + " " + self.item[:80]
    class Meta:
        db_table = u'DOC'

class Idx653A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX653a'

class Idx245Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX245aX'

class Docphase(models.Model):
    doc_id = models.IntegerField(null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    phase = models.IntegerField(null=True, db_column='PHASE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DOCPHASE'

class Extdicts(models.Model):
    caption = models.CharField(max_length=255, primary_key=True, db_column='CAPTION') # Field name made lowercase.
    query = models.CharField(max_length=255, db_column='QUERY', blank=True) # Field name made lowercase.
    colwidths = models.CharField(max_length=255, db_column='COLWIDTHS', blank=True) # Field name made lowercase.
    colnames = models.CharField(max_length=255, db_column='COLNAMES', blank=True) # Field name made lowercase.
    retval = models.CharField(max_length=255, db_column='RETVAL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EXTDICTS'

class Hand(models.Model):
    rdr_id = models.CharField(max_length=16, db_column='RDR_ID', blank=True) # Field name made lowercase.
    inv_id = models.IntegerField(null=True, db_column='INV_ID', blank=True) # Field name made lowercase.
    getdate = models.FloatField(null=True, db_column='GETDATE', blank=True) # Field name made lowercase.
    retdate = models.FloatField(null=True, db_column='RETDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HAND'

class Idx100A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX100a'

class Idx100Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX100aX'

class Publisher(models.Model):
    item = models.CharField(max_length=255, primary_key=True, db_column='ITEM') # Field name made lowercase.
    class Meta:
        db_table = u'PUBLISHER'
class Idx653Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX653aX'

