#
# PySNMP MIB module SNMP-USM-DH-OBJECTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-USM-DH-OBJECTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:27:40 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, experimental, Unsigned32, Bits, NotificationType, Integer32, ModuleIdentity, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "experimental", "Unsigned32", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmDHObjectsMIB = ModuleIdentity((1, 3, 6, 1, 3, 101))
snmpUsmDHObjectsMIB.setRevisions(('2000-03-06 00:00',))
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setOrganization('Excite@Home')
usmDHKeyObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1))
usmDHKeyConformance = MibIdentifier((1, 3, 6, 1, 3, 101, 2))
class DHKeyChange(TextualConvention, OctetString):
    reference = '-- Diffie-Hellman Key-Agreement Standard, PKCS #3; RSA Laboratories, November 1993'
    status = 'current'

usmDHPublicObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 1))
usmDHParameters = MibScalar((1, 3, 6, 1, 3, 101, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmDHParameters.setStatus('current')
usmDHUserKeyTable = MibTable((1, 3, 6, 1, 3, 101, 1, 1, 2), )
if mibBuilder.loadTexts: usmDHUserKeyTable.setStatus('current')
usmDHUserKeyEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 1, 2, 1), )
usmUserEntry.registerAugmentions(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserKeyEntry"))
usmDHUserKeyEntry.setIndexNames(*usmUserEntry.getIndexNames())
if mibBuilder.loadTexts: usmDHUserKeyEntry.setStatus('current')
usmDHUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 1), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserAuthKeyChange.setStatus('current')
usmDHUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 2), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnAuthKeyChange.setStatus('current')
usmDHUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 3), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserPrivKeyChange.setStatus('current')
usmDHUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 4), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnPrivKeyChange.setStatus('current')
usmDHKickstartGroup = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 2))
usmDHKickstartTable = MibTable((1, 3, 6, 1, 3, 101, 1, 2, 1), )
if mibBuilder.loadTexts: usmDHKickstartTable.setStatus('current')
usmDHKickstartEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 2, 1, 1), ).setIndexNames((0, "SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartIndex"))
if mibBuilder.loadTexts: usmDHKickstartEntry.setStatus('current')
usmDHKickstartIndex = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: usmDHKickstartIndex.setStatus('current')
usmDHKickstartMyPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setStatus('current')
usmDHKickstartMgrPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setStatus('current')
usmDHKickstartSecurityName = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartSecurityName.setStatus('current')
usmDHKeyMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 1))
usmDHKeyMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 2))
usmDHKeyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 101, 2, 1, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyMIBBasicGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyParamGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyKickstartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBCompliance = usmDHKeyMIBCompliance.setStatus('current')
usmDHKeyMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserPrivKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnPrivKeyChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBBasicGroup = usmDHKeyMIBBasicGroup.setStatus('current')
usmDHKeyParamGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 2)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHParameters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyParamGroup = usmDHKeyParamGroup.setStatus('current')
usmDHKeyKickstartGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 3)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMyPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMgrPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartSecurityName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyKickstartGroup = usmDHKeyKickstartGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-USM-DH-OBJECTS-MIB", usmDHUserPrivKeyChange=usmDHUserPrivKeyChange, usmDHKeyMIBCompliance=usmDHKeyMIBCompliance, usmDHKickstartIndex=usmDHKickstartIndex, snmpUsmDHObjectsMIB=snmpUsmDHObjectsMIB, usmDHUserKeyTable=usmDHUserKeyTable, usmDHKeyMIBGroups=usmDHKeyMIBGroups, usmDHKeyObjects=usmDHKeyObjects, usmDHKeyMIBBasicGroup=usmDHKeyMIBBasicGroup, usmDHKickstartTable=usmDHKickstartTable, usmDHKickstartEntry=usmDHKickstartEntry, usmDHKeyMIBCompliances=usmDHKeyMIBCompliances, usmDHParameters=usmDHParameters, usmDHUserOwnPrivKeyChange=usmDHUserOwnPrivKeyChange, usmDHUserOwnAuthKeyChange=usmDHUserOwnAuthKeyChange, usmDHKickstartSecurityName=usmDHKickstartSecurityName, usmDHKeyParamGroup=usmDHKeyParamGroup, usmDHPublicObjects=usmDHPublicObjects, DHKeyChange=DHKeyChange, usmDHUserKeyEntry=usmDHUserKeyEntry, usmDHKickstartGroup=usmDHKickstartGroup, usmDHKeyConformance=usmDHKeyConformance, usmDHKickstartMgrPublic=usmDHKickstartMgrPublic, usmDHKickstartMyPublic=usmDHKickstartMyPublic, usmDHKeyKickstartGroup=usmDHKeyKickstartGroup, usmDHUserAuthKeyChange=usmDHUserAuthKeyChange, PYSNMP_MODULE_ID=snmpUsmDHObjectsMIB)
