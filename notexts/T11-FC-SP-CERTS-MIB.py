#
# PySNMP MIB module T11-FC-SP-CERTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-SP-CERTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 14:59:44 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Integer32, Counter32, iso, Unsigned32, mib_2, Counter64, IpAddress, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Integer32", "Counter32", "iso", "Unsigned32", "mib-2", "Counter64", "IpAddress", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11FcSpAuEntityName, = mibBuilder.importSymbols("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcSpCertsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 1))
t11FcSpCertsMIB.setRevisions(('2007-02-19 00:00',))
if mibBuilder.loadTexts: t11FcSpCertsMIB.setLastUpdated('200702190000Z')
if mibBuilder.loadTexts: t11FcSpCertsMIB.setOrganization('T11')
t11FcSpCertsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 1))
t11FcSpCertsMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2))
t11FcSpCertsTable = MibTable((1, 3, 6, 1, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: t11FcSpCertsTable.setStatus('current')
t11FcSpCertsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"), (0, "T11-FC-SP-CERTS-MIB", "t11FcSpCertFabricIndex"), (0, "T11-FC-SP-CERTS-MIB", "t11FcSpCertIndex"))
if mibBuilder.loadTexts: t11FcSpCertsEntry.setStatus('current')
t11FcSpCertFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FcSpCertFabricIndex.setStatus('current')
t11FcSpCertIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: t11FcSpCertIndex.setStatus('current')
t11FcSpCertPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpCertPointer.setStatus('current')
t11FcSpCertUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ownDefaultCert", 2), ("ownCert", 3), ("rootCert", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpCertUsage.setStatus('current')
t11FcSpCertMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 1))
t11FcSpCertMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 2))
t11FcSpCertMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 1, 2, 1, 1)).setObjects(("T11-FC-SP-CERTS-MIB", "t11FcSpCertInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpCertMIBCompliance = t11FcSpCertMIBCompliance.setStatus('current')
t11FcSpCertInfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 1, 2, 2, 1)).setObjects(("T11-FC-SP-CERTS-MIB", "t11FcSpCertPointer"), ("T11-FC-SP-CERTS-MIB", "t11FcSpCertUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpCertInfoGroup = t11FcSpCertInfoGroup.setStatus('current')
mibBuilder.exportSymbols("T11-FC-SP-CERTS-MIB", t11FcSpCertsMIB=t11FcSpCertsMIB, t11FcSpCertMIBGroups=t11FcSpCertMIBGroups, t11FcSpCertsEntry=t11FcSpCertsEntry, t11FcSpCertUsage=t11FcSpCertUsage, t11FcSpCertMIBCompliances=t11FcSpCertMIBCompliances, PYSNMP_MODULE_ID=t11FcSpCertsMIB, t11FcSpCertPointer=t11FcSpCertPointer, t11FcSpCertsTable=t11FcSpCertsTable, t11FcSpCertMIBCompliance=t11FcSpCertMIBCompliance, t11FcSpCertInfoGroup=t11FcSpCertInfoGroup, t11FcSpCertsMIBConformance=t11FcSpCertsMIBConformance, t11FcSpCertFabricIndex=t11FcSpCertFabricIndex, t11FcSpCertIndex=t11FcSpCertIndex, t11FcSpCertsMIBObjects=t11FcSpCertsMIBObjects)
