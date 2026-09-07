#
# PySNMP MIB module DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB
# Source digest sha256:9d84a846c2af76d1bf12c39dc384a19eb13285b1c7b4df63ad8dc779cfd02f64
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwNetworkProtocolPortProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 194))
dlinkSwNetworkProtocolPortProtectMIB.setRevisions(('2017-11-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setRevisionsDescriptions((' This is the first version of the MIB file.\n            ',))
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setLastUpdated('2017-11-27 00:00')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setDescription('This MIB module defines objects for network protocol port protect.')
dNetworkProtocolPortProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1))
dNetworkProtocolPortProtectCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1))
dNetworkProtocolPortProtectTCPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectTCPState.setStatus('current')
if mibBuilder.loadTexts: dNetworkProtocolPortProtectTCPState.setDescription('When enable it switch will not response for the closed TCP port.')
dNetworkProtocolPortProtectUDPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectUDPState.setStatus('current')
if mibBuilder.loadTexts: dNetworkProtocolPortProtectUDPState.setDescription('When enable it switch will not response for the closed UDP port.')
mibBuilder.exportSymbols("DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB", PYSNMP_MODULE_ID=dlinkSwNetworkProtocolPortProtectMIB, dNetworkProtocolPortProtectCtrl=dNetworkProtocolPortProtectCtrl, dNetworkProtocolPortProtectObjects=dNetworkProtocolPortProtectObjects, dNetworkProtocolPortProtectTCPState=dNetworkProtocolPortProtectTCPState, dNetworkProtocolPortProtectUDPState=dNetworkProtocolPortProtectUDPState, dlinkSwNetworkProtocolPortProtectMIB=dlinkSwNetworkProtocolPortProtectMIB)
