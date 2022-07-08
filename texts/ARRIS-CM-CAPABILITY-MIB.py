#
# PySNMP MIB module ARRIS-CM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-CAPABILITY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 07:58:16 2022
# On host fv-az121-197 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity, ModuleIdentity, Counter32, MibIdentifier, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibIdentifier", "NotificationType", "TimeTicks")
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
mibBuilder.exportSymbols("ARRIS-CM-CAPABILITY-MIB", PYSNMP_MODULE_ID=modemCapabilities, modemAgentDocsis10=modemAgentDocsis10, modemCapabilities=modemCapabilities, modemCapabilitiesObjects=modemCapabilitiesObjects, modemAgentDocsis20=modemAgentDocsis20, modemAgentDocsis11=modemAgentDocsis11)
