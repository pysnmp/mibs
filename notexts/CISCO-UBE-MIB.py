#
# PySNMP MIB module CISCO-UBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-UBE-MIB
# Source digest sha256:bfe426947ad1be7ea995a87dd675367578961ad46ca036a465253bc6a5b8039d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoUbeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 764))
ciscoUbeMIB.setRevisions(('2010-11-29 00:00',))
if mibBuilder.loadTexts: ciscoUbeMIB.setLastUpdated('2010-11-29 00:00')
if mibBuilder.loadTexts: ciscoUbeMIB.setOrganization('Cisco Systems, Inc.')
ciscoUbeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 0))
ciscoUbeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1))
cubeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeEnabled.setStatus('current')
cubeVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cubeVersion.setStatus('current')
cubeTotalSessionAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setUnits('session').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setStatus('current')
ciscoUbeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1))
ciscoUbeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2))
ciscoCubeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)).setObjects(("CISCO-UBE-MIB", "ciscoUbeMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCubeMIBCompliance = ciscoCubeMIBCompliance.setStatus('current')
ciscoUbeMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)).setObjects(("CISCO-UBE-MIB", "cubeEnabled"), ("CISCO-UBE-MIB", "cubeVersion"), ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUbeMIBGroup = ciscoUbeMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-UBE-MIB", PYSNMP_MODULE_ID=ciscoUbeMIB, ciscoCubeMIBCompliance=ciscoCubeMIBCompliance, ciscoUbeMIB=ciscoUbeMIB, ciscoUbeMIBCompliances=ciscoUbeMIBCompliances, ciscoUbeMIBConform=ciscoUbeMIBConform, ciscoUbeMIBGroup=ciscoUbeMIBGroup, ciscoUbeMIBGroups=ciscoUbeMIBGroups, ciscoUbeMIBObjects=ciscoUbeMIBObjects, cubeEnabled=cubeEnabled, cubeTotalSessionAllowed=cubeTotalSessionAllowed, cubeVersion=cubeVersion)
