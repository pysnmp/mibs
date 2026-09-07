#
# PySNMP MIB module CISCO-GGSN-GEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GGSN-GEO-MIB
# Source digest sha256:f7ea70b680ee9300a2adc234a8ad0caa72c2004c1f80c5af76b4855418a6b320
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
cggsnGeoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 724))
cggsnGeoMIB.setRevisions(('2010-02-19 00:00',))
if mibBuilder.loadTexts: cggsnGeoMIB.setLastUpdated('2010-02-19 00:00')
if mibBuilder.loadTexts: cggsnGeoMIB.setOrganization('Cisco Systems, Inc.')
cggsnGeoPassiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 724, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cggsnGeoPassiveTable.setStatus('current')
cggsnGeoPassiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-GGSN-GEO-MIB", "cggsnGeoProcessNumber"))
if mibBuilder.loadTexts: cggsnGeoPassiveEntry.setStatus('current')
cggsnGeoProcessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cggsnGeoProcessNumber.setStatus('current')
cggsnGeoPassiveStdbyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveStdbyIfName.setStatus('current')
cggsnGeoPassiveIfOnStdby = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveIfOnStdby.setStatus('current')
cggsnGeoVRFEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cggsnGeoVRFEnabled.setStatus('current')
cggsnGeoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoRowStatus.setStatus('current')
cggsnGeoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2))
cggsnGeogroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1))
cggsnGeoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2))
cggsnGeoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoCompliance = cggsnGeoCompliance.setStatus('current')
cggsnGeoPassiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveStdbyIfName"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveIfOnStdby"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoVRFEnabled"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoPassiveGroup = cggsnGeoPassiveGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-GEO-MIB", PYSNMP_MODULE_ID=cggsnGeoMIB, cggsnGeoCompliance=cggsnGeoCompliance, cggsnGeoCompliances=cggsnGeoCompliances, cggsnGeoConformance=cggsnGeoConformance, cggsnGeoMIB=cggsnGeoMIB, cggsnGeoPassiveEntry=cggsnGeoPassiveEntry, cggsnGeoPassiveGroup=cggsnGeoPassiveGroup, cggsnGeoPassiveIfOnStdby=cggsnGeoPassiveIfOnStdby, cggsnGeoPassiveStdbyIfName=cggsnGeoPassiveStdbyIfName, cggsnGeoPassiveTable=cggsnGeoPassiveTable, cggsnGeoProcessNumber=cggsnGeoProcessNumber, cggsnGeoRowStatus=cggsnGeoRowStatus, cggsnGeoVRFEnabled=cggsnGeoVRFEnabled, cggsnGeogroups=cggsnGeogroups)
