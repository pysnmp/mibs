#
# PySNMP MIB module LINKSYS-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-DEBUGCAPABILITIES-MIB
# Source digest sha256:2b2f119a022c69a54d8349c448c774c6489be4679afba48867713d266ab61cea
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDebugCapabilities.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('2011-01-05 00:00')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlDebugCapabilities.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlDebugCapabilities.setDescription('This private MIB module is used for achieving extended\n                      debugging capablities for the device.\n                      For example: greater management capabilies for technical\n                      support users.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setDescription('A user intereseted to obtain extended debug capabilities should\n            SET this MIB to a well known secret value (it is intended to be\n            used only by authorized users).\n            Most often, this value will be based on the device MAC address.\n            Upon setting the correct value, the SET operation will return\n            noError. Otherwise, wrongValue will return to the caller.\n            GET operation on this MIB will reurn a value of length 0.')
mibBuilder.exportSymbols("LINKSYS-DEBUGCAPABILITIES-MIB", PYSNMP_MODULE_ID=rlDebugCapabilities, rlDebugCapabilities=rlDebugCapabilities, rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword)
