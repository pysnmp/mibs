#
# PySNMP MIB module ARRIS-CM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Wed May 29 02:40:24 2024
# On host fv-az569-426 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, NotificationType, Unsigned32, IpAddress, MibIdentifier, iso, Integer32, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Integer32", "TimeTicks", "Bits", "Counter32")
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
mibBuilder.exportSymbols("ARRIS-CM-CAPABILITY-MIB", PYSNMP_MODULE_ID=modemCapabilities, modemCapabilities=modemCapabilities, modemAgentDocsis11=modemAgentDocsis11, modemAgentDocsis10=modemAgentDocsis10, modemCapabilitiesObjects=modemCapabilitiesObjects, modemAgentDocsis20=modemAgentDocsis20)
