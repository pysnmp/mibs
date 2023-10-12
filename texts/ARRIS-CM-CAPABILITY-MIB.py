#
# PySNMP MIB module ARRIS-CM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-CAPABILITY-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 09:01:55 2023
# On host fv-az245-3 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, ModuleIdentity, Gauge32, Unsigned32, NotificationType, IpAddress, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "TimeTicks", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
modemCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20))
if mibBuilder.loadTexts: modemCapabilities.setLastUpdated('0206250000Z')
if mibBuilder.loadTexts: modemCapabilities.setOrganization('Arris Interactive, L.L.C.')
if mibBuilder.loadTexts: modemCapabilities.setContactInfo('Robert Coley\n       Postal: Arris Interactive, L.L.C.\n               3871 Lakefield Drive\n               Suite 300\n               Suwanee, GA 30024-1242\n               U.S.A.\n       Phone:  +1 770 622 8500\n       E-mail: robert.coley@arrisi.com')
if mibBuilder.loadTexts: modemCapabilities.setDescription('This is the MIB Module describing modem capabilities.')
modemCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1))
modemAgentDocsis10 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 1))
modemAgentDocsis11 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 2))
modemAgentDocsis20 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 3))
mibBuilder.exportSymbols("ARRIS-CM-CAPABILITY-MIB", PYSNMP_MODULE_ID=modemCapabilities, modemAgentDocsis11=modemAgentDocsis11, modemAgentDocsis20=modemAgentDocsis20, modemAgentDocsis10=modemAgentDocsis10, modemCapabilities=modemCapabilities, modemCapabilitiesObjects=modemCapabilitiesObjects)
