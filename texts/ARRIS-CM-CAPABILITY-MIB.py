#
# PySNMP MIB module ARRIS-CM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-CAPABILITY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:11 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, iso, Integer32, Unsigned32, Counter32, IpAddress, MibIdentifier, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "iso", "Integer32", "Unsigned32", "Counter32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
modemCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20))
if mibBuilder.loadTexts: modemCapabilities.setLastUpdated('0206250000Z')
if mibBuilder.loadTexts: modemCapabilities.setOrganization('Arris Interactive, L.L.C.')
if mibBuilder.loadTexts: modemCapabilities.setContactInfo('Robert Coley\n       Postal: Arris Interactive, L.L.C.\n               3871 Lakefield Drive\n               Suite 300\n               Suwanee, GA 30024-1242\n               U.S.A.\n       Phone:  +1 770 622 8500\n       E-mail: robert.coley@arrisi.com')
if mibBuilder.loadTexts: modemCapabilities.setDescription('This is the MIB Module describing modem capabilities.')
modemCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1))
modemAgentDocsis10 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 1))
modemAgentDocsis11 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 2))
modemAgentDocsis20 = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 20, 1, 3))
mibBuilder.exportSymbols("ARRIS-CM-CAPABILITY-MIB", PYSNMP_MODULE_ID=modemCapabilities, modemCapabilitiesObjects=modemCapabilitiesObjects, modemAgentDocsis10=modemAgentDocsis10, modemAgentDocsis20=modemAgentDocsis20, modemAgentDocsis11=modemAgentDocsis11, modemCapabilities=modemCapabilities)
