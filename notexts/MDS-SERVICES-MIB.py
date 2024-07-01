#
# PySNMP MIB module MDS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICES-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 11:13:29 2024
# On host fv-az1493-704 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, ModuleIdentity, IpAddress, Integer32, Gauge32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Bits, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Bits", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdsServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1))
mdsServicesMIB.setRevisions(('2018-05-16 00:00', '2014-10-20 00:00', '2014-05-12 00:00',))
if mibBuilder.loadTexts: mdsServicesMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsServicesMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1))
mServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 1))
mServStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2))
mServStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: mServStatusTable.setStatus('current')
mServStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "MDS-SERVICES-MIB", "mServServiceName"))
if mibBuilder.loadTexts: mServStatusEntry.setStatus('current')
mServServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServServiceName.setStatus('current')
mServServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("running", 0), ("disabled", 1), ("error", 2), ("notRunning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServServiceStatus.setStatus('current')
mdsServMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3))
mdsServMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1))
mdsServMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2))
mServCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1, 1)).setObjects(("MDS-SERVICES-MIB", "mServStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mServCompliance = mServCompliance.setStatus('current')
mServStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2, 1)).setObjects(("MDS-SERVICES-MIB", "mServServiceName"), ("MDS-SERVICES-MIB", "mServServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mServStatusGroup = mServStatusGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-SERVICES-MIB", mServStatusEntry=mServStatusEntry, mServConfig=mServConfig, mdsServMIBConformance=mdsServMIBConformance, mdsServicesMIB=mdsServicesMIB, mdsServMIBCompliances=mdsServMIBCompliances, mServStatusGroup=mServStatusGroup, mServStatusTable=mServStatusTable, mServMIBObjects=mServMIBObjects, mServServiceName=mServServiceName, mServServiceStatus=mServServiceStatus, mServCompliance=mServCompliance, PYSNMP_MODULE_ID=mdsServicesMIB, mdsServMIBGroups=mdsServMIBGroups, mServStatus=mServStatus)
