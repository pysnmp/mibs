#
# PySNMP MIB module SNMP-USM-DH-OBJECTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SNMP-USM-DH-OBJECTS-MIB
# Source digest sha256:c09635600c53253308326e924c3f6982a0b4f8f9dd2fe3b4e0313d9fed0a1258
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, experimental, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "experimental", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmDHObjectsMIB = ModuleIdentity((1, 3, 6, 1, 3, 101))
snmpUsmDHObjectsMIB.setRevisions(('2000-03-06 00:00',))
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setLastUpdated('2000-03-06 00:00')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setOrganization('Excite@Home')
usmDHKeyObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1))
usmDHKeyConformance = MibIdentifier((1, 3, 6, 1, 3, 101, 2))
class DHKeyChange(TextualConvention, OctetString):
    reference = '-- Diffie-Hellman Key-Agreement Standard, PKCS #3; RSA Laboratories, November 1993'
    status = 'current'

usmDHPublicObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 1))
usmDHParameters = MibScalar((1, 3, 6, 1, 3, 101, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmDHParameters.setStatus('current')
usmDHUserKeyTable = MibTable((1, 3, 6, 1, 3, 101, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: usmDHUserKeyTable.setStatus('current')
usmDHUserKeyEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 1, 2, 1), ).setMaxAccess("notaccessible")
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
usmDHKickstartTable = MibTable((1, 3, 6, 1, 3, 101, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: usmDHKickstartTable.setStatus('current')
usmDHKickstartEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartIndex"))
if mibBuilder.loadTexts: usmDHKickstartEntry.setStatus('current')
usmDHKickstartIndex = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
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
mibBuilder.exportSymbols("SNMP-USM-DH-OBJECTS-MIB", DHKeyChange=DHKeyChange, PYSNMP_MODULE_ID=snmpUsmDHObjectsMIB, snmpUsmDHObjectsMIB=snmpUsmDHObjectsMIB, usmDHKeyConformance=usmDHKeyConformance, usmDHKeyKickstartGroup=usmDHKeyKickstartGroup, usmDHKeyMIBBasicGroup=usmDHKeyMIBBasicGroup, usmDHKeyMIBCompliance=usmDHKeyMIBCompliance, usmDHKeyMIBCompliances=usmDHKeyMIBCompliances, usmDHKeyMIBGroups=usmDHKeyMIBGroups, usmDHKeyObjects=usmDHKeyObjects, usmDHKeyParamGroup=usmDHKeyParamGroup, usmDHKickstartEntry=usmDHKickstartEntry, usmDHKickstartGroup=usmDHKickstartGroup, usmDHKickstartIndex=usmDHKickstartIndex, usmDHKickstartMgrPublic=usmDHKickstartMgrPublic, usmDHKickstartMyPublic=usmDHKickstartMyPublic, usmDHKickstartSecurityName=usmDHKickstartSecurityName, usmDHKickstartTable=usmDHKickstartTable, usmDHParameters=usmDHParameters, usmDHPublicObjects=usmDHPublicObjects, usmDHUserAuthKeyChange=usmDHUserAuthKeyChange, usmDHUserKeyEntry=usmDHUserKeyEntry, usmDHUserKeyTable=usmDHUserKeyTable, usmDHUserOwnAuthKeyChange=usmDHUserOwnAuthKeyChange, usmDHUserOwnPrivKeyChange=usmDHUserOwnPrivKeyChange, usmDHUserPrivKeyChange=usmDHUserPrivKeyChange)
