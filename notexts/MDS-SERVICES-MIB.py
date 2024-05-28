#
# PySNMP MIB module MDS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICES-MIB
# Produced by pysmi-1.1.12 at Tue May 28 11:47:29 2024
# On host fv-az665-912 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Bits, IpAddress, Gauge32, MibIdentifier, Integer32, Counter32, iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MDS-SERVICES-MIB", mServStatusEntry=mServStatusEntry, PYSNMP_MODULE_ID=mdsServicesMIB, mdsServicesMIB=mdsServicesMIB, mServCompliance=mServCompliance, mServServiceName=mServServiceName, mServStatusGroup=mServStatusGroup, mServMIBObjects=mServMIBObjects, mServStatusTable=mServStatusTable, mdsServMIBConformance=mdsServMIBConformance, mdsServMIBGroups=mdsServMIBGroups, mServStatus=mServStatus, mdsServMIBCompliances=mdsServMIBCompliances, mServServiceStatus=mServServiceStatus, mServConfig=mServConfig)
