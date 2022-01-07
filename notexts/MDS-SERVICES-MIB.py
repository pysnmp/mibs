#
# PySNMP MIB module MDS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICES-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 01:08:06 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, IpAddress, iso, Gauge32, Counter64, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "Gauge32", "Counter64", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Integer32", "Counter32")
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
mibBuilder.exportSymbols("MDS-SERVICES-MIB", mServStatus=mServStatus, mdsServMIBCompliances=mdsServMIBCompliances, mdsServicesMIB=mdsServicesMIB, mServServiceName=mServServiceName, mdsServMIBGroups=mdsServMIBGroups, PYSNMP_MODULE_ID=mdsServicesMIB, mServServiceStatus=mServServiceStatus, mServStatusGroup=mServStatusGroup, mServStatusEntry=mServStatusEntry, mServStatusTable=mServStatusTable, mdsServMIBConformance=mdsServMIBConformance, mServConfig=mServConfig, mServCompliance=mServCompliance, mServMIBObjects=mServMIBObjects)
