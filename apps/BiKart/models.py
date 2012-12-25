# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Econttypes(models.Model):
    ttype = models.IntegerField(primary_key=True, db_column='TTYPE') # Field name made lowercase.
    sname = models.CharField(max_length=32, db_column='SNAME', blank=True) # Field name made lowercase.
    lname = models.CharField(max_length=100, db_column='LNAME', blank=True) # Field name made lowercase.
    rtype = models.IntegerField(null=True, db_column='RTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ECONTTYPES'

class Idx100A(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX100a'

class T1C5Fd401(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1C5FD40_1'

class Environment(models.Model):
    maincode = models.CharField(max_length=255, db_column='MainCode', blank=True) # Field name made lowercase.
    mainname = models.CharField(max_length=255, db_column='MainName', blank=True) # Field name made lowercase.
    secondcode = models.CharField(max_length=255, db_column='SecondCode', blank=True) # Field name made lowercase.
    secondname = models.CharField(max_length=255, db_column='SecondName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ENVIRONMENT'

class Idx100Ax(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX100aX'

class Staff(models.Model):
    login = models.CharField(max_length=32, primary_key=True, db_column='LOGIN') # Field name made lowercase.
    password = models.CharField(max_length=32, db_column='PASSWORD', blank=True) # Field name made lowercase.
    grp = models.IntegerField(null=True, db_column='GRP', blank=True) # Field name made lowercase.
    acc = models.IntegerField(null=True, db_column='ACC', blank=True) # Field name made lowercase.
    acc2 = models.IntegerField(null=True, db_column='ACC2', blank=True) # Field name made lowercase.
    phase = models.IntegerField(null=True, db_column='PHASE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'STAFF'

class Extdicts(models.Model):
    caption = models.CharField(max_length=255, primary_key=True, db_column='CAPTION') # Field name made lowercase.
    query = models.TextField(db_column='QUERY', blank=True) # Field name made lowercase.
    colwidths = models.CharField(max_length=255, db_column='COLWIDTHS', blank=True) # Field name made lowercase.
    colnames = models.CharField(max_length=255, db_column='COLNAMES', blank=True) # Field name made lowercase.
    retval = models.CharField(max_length=255, db_column='RETVAL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EXTDICTS'

class Idx245A(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX245a'

class Timetable(models.Model):
    grp = models.ForeignKey(Grp, null=True, db_column='GRP_ID', blank=True) # Field name made lowercase.
    period = models.IntegerField(null=True, db_column='PERIOD', blank=True) # Field name made lowercase.
    discp = models.ForeignKey(Discp, null=True, db_column='DISCP_ID', blank=True) # Field name made lowercase.
    teacher = models.CharField(max_length=255, db_column='TEACHER', blank=True) # Field name made lowercase.
    room = models.CharField(max_length=255, db_column='ROOM', blank=True) # Field name made lowercase.
    day = models.IntegerField(null=True, db_column='DAY', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TIMETABLE'

class Grp(models.Model):
    grp_id = models.IntegerField(primary_key=True, db_column='GRP_ID') # Field name made lowercase.
    spec = models.ForeignKey(Spec, null=True, db_column='SPEC_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=255, db_column='CHIEF', blank=True) # Field name made lowercase.
    educform = models.IntegerField(null=True, db_column='EDUCFORM', blank=True) # Field name made lowercase.
    course = models.IntegerField(null=True, db_column='COURSE', blank=True) # Field name made lowercase.
    semstr = models.IntegerField(null=True, db_column='SEMSTR', blank=True) # Field name made lowercase.
    quantity = models.IntegerField(null=True, db_column='QUANTITY', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    typegrp = models.IntegerField(null=True, db_column='TYPEGRP', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'GRP'

class Idx245Ax(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX245aX'

class Sxhelp(models.Model):
    did = models.ForeignKey(Sxterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    dhelp = models.CharField(max_length=100, db_column='DHELP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SXHELP'

class Idx653A(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX653a'

class Sxrefs(models.Model):
    did = models.ForeignKey(Sxterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    tid = models.ForeignKey(Sxterms, null=True, db_column='TID', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Sxttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SXREFS'

class Discp(models.Model):
    discp_id = models.IntegerField(primary_key=True, db_column='DISCP_ID') # Field name made lowercase.
    chair = models.ForeignKey(Chair, null=True, db_column='CHAIR_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    cypher = models.IntegerField(null=True, db_column='CYPHER', blank=True) # Field name made lowercase.
    spcph_id = models.IntegerField(null=True, db_column='SPCPH_ID', blank=True) # Field name made lowercase.
    drct_id = models.IntegerField(null=True, db_column='DRCT_ID', blank=True) # Field name made lowercase.
    cycl_id = models.IntegerField(null=True, db_column='CYCL_ID', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DISCP'

class Sxterms(models.Model):
    tid = models.AutoField(primary_key=True, db_column='TID') # Field name made lowercase.
    term = models.CharField(max_length=255, db_column='TERM', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Sxttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SXTERMS'

class Idx653Ax(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX653aX'

class T2989A501(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2989A50_1'

class Idx773T(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX773t'

class Sxttypes(models.Model):
    ttype = models.IntegerField(primary_key=True, db_column='TTYPE') # Field name made lowercase.
    sname = models.CharField(max_length=32, db_column='SNAME', blank=True) # Field name made lowercase.
    lname = models.CharField(max_length=100, db_column='LNAME', blank=True) # Field name made lowercase.
    rtype = models.IntegerField(null=True, db_column='RTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SXTTYPES'

class Mathematics(models.Model):
    code_id = models.AutoField(primary_key=True, db_column='Code_ID') # Field name made lowercase.
    maincode = models.CharField(max_length=255, db_column='MainCode', blank=True) # Field name made lowercase.
    mainname = models.CharField(max_length=255, db_column='MainName', blank=True) # Field name made lowercase.
    secondcode = models.CharField(max_length=255, db_column='SecondCode', blank=True) # Field name made lowercase.
    secondname = models.CharField(max_length=255, db_column='SecondName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MATHEMATICS'

class Idx090A(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX090a'

class T150126B3(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_150126B_3'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, unique=True)
    principal_id = models.IntegerField(unique=True)
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(null=True, blank=True)
    definition = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'sysdiagrams'

class T1Cff1391(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1CFF139_1'

class Idx900A(models.Model):
    idx_id = models.AutoField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX900a'

class T176290A23(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_176290A_23'

class T1D591C41(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1D591C4_1'

class Hand(models.Model):
    rdr_id = models.CharField(max_length=16, db_column='RDR_ID', blank=True) # Field name made lowercase.
    inv_id = models.IntegerField(null=True, db_column='INV_ID', blank=True) # Field name made lowercase.
    getdate = models.FloatField(null=True, db_column='GETDATE', blank=True) # Field name made lowercase.
    retdate = models.FloatField(null=True, db_column='RETDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HAND'

class T1Aba49F2(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1ABA49F_2'

class T1E4Fdb210(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1E4FDB2_10'

class Inv(models.Model):
    inv_id = models.AutoField(primary_key=True, db_column='INV_ID') # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
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
    class Meta:
        db_table = u'INV'

class T1Aee9F71(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1AEE9F7_1'

class T23D452E1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_23D452E_1'

class Invoff(models.Model):
    inv_id = models.IntegerField(db_column='INV_ID') # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
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
    class Meta:
        db_table = u'INVOFF'

class T1Af8A8C1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1AF8A8C_1'

class T24E213B1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_24E213B_1'

class Lowbbk(models.Model):
    did = models.ForeignKey(Lowterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    bbk = models.CharField(max_length=100, db_column='BBK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOWBBK'

class Spec(models.Model):
    spec_id = models.IntegerField(primary_key=True, db_column='SPEC_ID') # Field name made lowercase.
    chair = models.ForeignKey(Chair, null=True, db_column='CHAIR_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    cypher = models.IntegerField(null=True, db_column='CYPHER', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=255, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=255, db_column='CHIEF', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SPEC'

class Lowhelp(models.Model):
    did = models.ForeignKey(Lowterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    dhelp = models.CharField(max_length=100, db_column='DHELP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOWHELP'

class T252622B69(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_252622B_69'

class Lowrefs(models.Model):
    did = models.ForeignKey(Lowterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    tid = models.ForeignKey(Lowterms, null=True, db_column='TID', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Lowttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOWREFS'

class T26906D41(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_26906D4_1'

class Lowterms(models.Model):
    tid = models.AutoField(primary_key=True, db_column='TID') # Field name made lowercase.
    term = models.CharField(max_length=255, db_column='TERM', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Lowttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOWTERMS'

class T1Bf3A4B1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1BF3A4B_1'

class Lowttypes(models.Model):
    ttype = models.IntegerField(primary_key=True, db_column='TTYPE') # Field name made lowercase.
    sname = models.CharField(max_length=32, db_column='SNAME', blank=True) # Field name made lowercase.
    lname = models.CharField(max_length=100, db_column='LNAME', blank=True) # Field name made lowercase.
    rtype = models.IntegerField(null=True, db_column='RTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOWTTYPES'

class T2811D1467(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2811D14_67'

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

class T1B8Ef361(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_1B8EF36_1'

class Acqu(models.Model):
    acq_id = models.AutoField(primary_key=True, db_column='ACQ_ID') # Field name made lowercase.
    doc_id = models.IntegerField(null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    src_id = models.IntegerField(null=True, db_column='SRC_ID', blank=True) # Field name made lowercase.
    ordered = models.IntegerField(null=True, db_column='ORDERED', blank=True) # Field name made lowercase.
    acquired = models.IntegerField(null=True, db_column='ACQUIRED', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    acqdate = models.FloatField(null=True, db_column='ACQDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQU'

class T29Af3F51(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_29AF3F5_1'

class Idx773Tx(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX773tX'

class T2A4202A1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2A4202A_1'

class Doc(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    rectype = models.CharField(max_length=1, db_column='RECTYPE', blank=True) # Field name made lowercase.
    biblevel = models.CharField(max_length=1, db_column='BIBLEVEL', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DOC'

class T2B98Ec456(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2B98EC4_56'

class Acqugot(models.Model):
    got_id = models.IntegerField(primary_key=True, db_column='GOT_ID') # Field name made lowercase.
    ord_id = models.IntegerField(null=True, db_column='ORD_ID', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    gotdate = models.FloatField(null=True, db_column='GOTDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQUGOT'

class T2F6E08A40(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2F6E08A_40'

class Acquord(models.Model):
    ord_id = models.IntegerField(primary_key=True, db_column='ORD_ID') # Field name made lowercase.
    doc_id = models.IntegerField(null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    src = models.CharField(max_length=255, db_column='SRC', blank=True) # Field name made lowercase.
    publ = models.CharField(max_length=255, db_column='PUBL', blank=True) # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    price = models.IntegerField(null=True, db_column='PRICE', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    getdate = models.FloatField(null=True, db_column='GETDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACQUORD'

class T2F7907042(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2F79070_42'

class Acqusrc(models.Model):
    item = models.CharField(max_length=255, primary_key=True, db_column='ITEM') # Field name made lowercase.
    class Meta:
        db_table = u'ACQUSRC'

class T32864051(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_3286405_1'

class Chair(models.Model):
    chair_id = models.IntegerField(primary_key=True, db_column='CHAIR_ID') # Field name made lowercase.
    dep = models.ForeignKey(Dep, null=True, db_column='DEP_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=255, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=255, db_column='CHIEF', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CHAIR'

class T3293Eaf1(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_3293EAF_1'

class CodeCountry(models.Model):
    nameeng = models.CharField(max_length=255, db_column='NameEng', blank=True) # Field name made lowercase.
    namerus = models.CharField(max_length=255, db_column='NameRus', blank=True) # Field name made lowercase.
    codecont = models.CharField(max_length=255, db_column='CodeCont', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CODE_COUNTRY'

class T332Cd3E43(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_332CD3E_43'

class CodeLanguage(models.Model):
    namerus = models.CharField(max_length=255, db_column='NameRus', blank=True) # Field name made lowercase.
    nameeng = models.CharField(max_length=255, db_column='NameEng', blank=True) # Field name made lowercase.
    codelang = models.CharField(max_length=255, db_column='CodeLang', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CODE_LANGUAGE'

class Tag(models.Model):
    tag = models.CharField(max_length=3, primary_key=True, db_column='TAG') # Field name made lowercase.
    subtag = models.CharField(max_length=1, primary_key=True, db_column='SUBTAG') # Field name made lowercase.
    flags = models.IntegerField(null=True, db_column='FLAGS', blank=True) # Field name made lowercase.
    separator = models.CharField(max_length=1, db_column='SEPARATOR', blank=True) # Field name made lowercase.
    caption = models.CharField(max_length=40, db_column='CAPTION', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TAG'

class Dbres(models.Model):
    name = models.CharField(max_length=16, primary_key=True, db_column='NAME') # Field name made lowercase.
    ires = models.IntegerField(null=True, db_column='IRES', blank=True) # Field name made lowercase.
    tres = models.CharField(max_length=255, db_column='TRES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DBRES'

class T27682151(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'T_2768215_1'

class Dep(models.Model):
    dep_id = models.IntegerField(primary_key=True, db_column='DEP_ID') # Field name made lowercase.
    plant = models.ForeignKey(Plant, null=True, db_column='PLANT_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=255, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=255, db_column='CHIEF', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DEP'

class Sxbbk(models.Model):
    did = models.ForeignKey(Sxterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    bbk = models.CharField(max_length=100, db_column='BBK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SXBBK'

class Idx090Ax(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX090aX'

class Orders(models.Model):
    rdr_id = models.CharField(max_length=16, db_column='RDR_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    sigla = models.CharField(max_length=255, db_column='SIGLA', blank=True) # Field name made lowercase.
    orddate = models.FloatField(null=True, db_column='ORDDATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ORDERS'

class Discpx(models.Model):
    discp = models.ForeignKey(Discp, null=True, db_column='DISCP_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    sign = models.IntegerField(null=True, db_column='SIGN', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DISCPX'

class Phisics(models.Model):
    maincode = models.CharField(max_length=255, db_column='MainCode', blank=True) # Field name made lowercase.
    mainname = models.CharField(max_length=255, db_column='MainName', blank=True) # Field name made lowercase.
    secondcode = models.CharField(max_length=255, db_column='SecondCode', blank=True) # Field name made lowercase.
    secondname = models.CharField(max_length=255, db_column='SecondName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PHISICS'

class Mobject(models.Model):
    name = models.CharField(max_length=255, primary_key=True, db_column='NAME') # Field name made lowercase.
    typ = models.CharField(max_length=64, db_column='TYP') # Field name made lowercase.
    siz = models.IntegerField(null=True, db_column='SIZ', blank=True) # Field name made lowercase.
    crdate = models.FloatField(null=True, db_column='CRDATE', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'MOBJECT'

class Plant(models.Model):
    plant_id = models.IntegerField(primary_key=True, db_column='PLANT_ID') # Field name made lowercase.
    root_id = models.IntegerField(null=True, db_column='ROOT_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    subrdn = models.CharField(max_length=255, db_column='SUBRDN', blank=True) # Field name made lowercase.
    branch = models.CharField(max_length=255, db_column='BRANCH', blank=True) # Field name made lowercase.
    region = models.CharField(max_length=255, db_column='REGION', blank=True) # Field name made lowercase.
    pstidx = models.CharField(max_length=50, db_column='PSTIDX', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=255, db_column='CITY', blank=True) # Field name made lowercase.
    adrp = models.CharField(max_length=255, db_column='ADRP', blank=True) # Field name made lowercase.
    phcode = models.CharField(max_length=50, db_column='PHCODE', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=50, db_column='PHONE', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=50, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255, db_column='EMAIL', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=255, db_column='WWW', blank=True) # Field name made lowercase.
    chief = models.CharField(max_length=255, db_column='CHIEF', blank=True) # Field name made lowercase.
    dateentry = models.FloatField(null=True, db_column='DATEENTRY', blank=True) # Field name made lowercase.
    custom1 = models.CharField(max_length=255, db_column='CUSTOM1', blank=True) # Field name made lowercase.
    custom2 = models.CharField(max_length=255, db_column='CUSTOM2', blank=True) # Field name made lowercase.
    custom3 = models.CharField(max_length=255, db_column='CUSTOM3', blank=True) # Field name made lowercase.
    numcst1 = models.IntegerField(null=True, db_column='NUMCST1', blank=True) # Field name made lowercase.
    numcst2 = models.IntegerField(null=True, db_column='NUMCST2', blank=True) # Field name made lowercase.
    numcst3 = models.IntegerField(null=True, db_column='NUMCST3', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PLANT'

class Docphase(models.Model):
    doc_id = models.IntegerField(null=True, db_column='DOC_ID', blank=True) # Field name made lowercase.
    phase = models.IntegerField(null=True, db_column='PHASE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DOCPHASE'

class Publisher(models.Model):
    item = models.CharField(max_length=255, primary_key=True, db_column='ITEM') # Field name made lowercase.
    class Meta:
        db_table = u'PUBLISHER'

class Econbbk(models.Model):
    did = models.ForeignKey(Econterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    bbk = models.CharField(max_length=100, db_column='BBK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ECONBBK'

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

class Econhelp(models.Model):
    did = models.ForeignKey(Econterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    dhelp = models.CharField(max_length=100, db_column='DHELP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ECONHELP'

class Econrefs(models.Model):
    did = models.ForeignKey(Econterms, null=True, db_column='DID', blank=True) # Field name made lowercase.
    tid = models.ForeignKey(Econterms, null=True, db_column='TID', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Econttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ECONREFS'

class Idx900Ax(models.Model):
    idx_id = models.IntegerField(null=True, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX900aX'

class Siglas(models.Model):
    id = models.IntegerField(null=True, db_column='ID', blank=True) # Field name made lowercase.
    fullname = models.CharField(max_length=255, db_column='FULLNAME', blank=True) # Field name made lowercase.
    shortname = models.CharField(max_length=255, db_column='SHORTNAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SIGLAS'

class Econterms(models.Model):
    tid = models.AutoField(primary_key=True, db_column='TID') # Field name made lowercase.
    term = models.CharField(max_length=255, db_column='TERM', blank=True) # Field name made lowercase.
    ttype = models.ForeignKey(Econttypes, null=True, db_column='TTYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ECONTERMS'

class Metaidx(models.Model):
    name = models.CharField(max_length=32, primary_key=True, db_column='NAME') # Field name made lowercase.
    type = models.CharField(max_length=32, db_column='TYPE') # Field name made lowercase.
    maxlen = models.IntegerField(null=True, db_column='MAXLEN', blank=True) # Field name made lowercase.
    tags = models.CharField(max_length=40, db_column='TAGS', blank=True) # Field name made lowercase.
    caption = models.CharField(max_length=50, db_column='CAPTION', blank=True) # Field name made lowercase.
    sep = models.CharField(max_length=64, db_column='SEP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'METAIDX'

class Source(models.Model):
    src_id = models.AutoField(primary_key=True, db_column='SRC_ID') # Field name made lowercase.
    name = models.CharField(max_length=255, db_column='NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SOURCE'

