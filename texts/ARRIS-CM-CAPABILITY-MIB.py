#
# PySNMP MIB module ARRIS-CM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 08:51:52 2024
# On host fv-az1149-759 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, NotificationType, ObjectIdentity, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, MibIdentifier, IpAddress, Counter32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "MibIdentifier", "IpAddress", "Counter32", "iso", "Gauge32")
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
mibBuilder.exportSymbols("ARRIS-CM-CAPABILITY-MIB", modemAgentDocsis11=modemAgentDocsis11, PYSNMP_MODULE_ID=modemCapabilities, modemAgentDocsis20=modemAgentDocsis20, modemAgentDocsis10=modemAgentDocsis10, modemCapabilitiesObjects=modemCapabilitiesObjects, modemCapabilities=modemCapabilities)
