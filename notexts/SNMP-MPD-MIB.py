#
# PySNMP MIB module SNMP-MPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-MPD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:09 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, NotificationType, ObjectIdentity, Counter32, Counter64, Gauge32, Unsigned32, MibIdentifier, snmpModules, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "NotificationType", "ObjectIdentity", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "snmpModules", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpMPDMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 11))
snmpMPDMIB.setRevisions(('2002-10-14 00:00', '1999-05-04 16:36', '1997-09-30 00:00',))
if mibBuilder.loadTexts: snmpMPDMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpMPDMIB.setOrganization('SNMPv3 Working Group')
snmpMPDAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 1))
snmpMPDMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2))
snmpMPDMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3))
snmpMPDStats = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2, 1))
snmpUnknownSecurityModels = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setStatus('current')
snmpInvalidMsgs = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInvalidMsgs.setStatus('current')
snmpUnknownPDUHandlers = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setStatus('current')
snmpMPDMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 1))
snmpMPDMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 2))
snmpMPDCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 11, 3, 1, 1)).setObjects(("SNMP-MPD-MIB", "snmpMPDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDCompliance = snmpMPDCompliance.setStatus('current')
snmpMPDGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 11, 3, 2, 1)).setObjects(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"), ("SNMP-MPD-MIB", "snmpInvalidMsgs"), ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDGroup = snmpMPDGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDStats=snmpMPDStats, snmpUnknownSecurityModels=snmpUnknownSecurityModels, snmpMPDCompliance=snmpMPDCompliance, snmpMPDMIBConformance=snmpMPDMIBConformance, PYSNMP_MODULE_ID=snmpMPDMIB, snmpUnknownPDUHandlers=snmpUnknownPDUHandlers, snmpMPDMIBObjects=snmpMPDMIBObjects, snmpMPDMIBCompliances=snmpMPDMIBCompliances, snmpInvalidMsgs=snmpInvalidMsgs, snmpMPDGroup=snmpMPDGroup, snmpMPDMIB=snmpMPDMIB, snmpMPDAdmin=snmpMPDAdmin, snmpMPDMIBGroups=snmpMPDMIBGroups)
