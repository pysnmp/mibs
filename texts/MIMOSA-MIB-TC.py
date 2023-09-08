#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.8 at Fri Sep  8 08:04:47 2023
# On host fv-az887-856 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, MibIdentifier, Counter32, Bits, Unsigned32, iso, ModuleIdentity, Integer32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "Counter32", "Bits", "Unsigned32", "iso", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mimosaMibTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 3))
mimosaMibTC.setRevisions(('2017-02-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mimosaMibTC.setRevisionsDescriptions(('First Revision of Textual Conventions defined for MIMOSA-MIB modules.',))
if mibBuilder.loadTexts: mimosaMibTC.setLastUpdated('201702150000Z')
if mibBuilder.loadTexts: mimosaMibTC.setOrganization('Mimosa Networks\n    \t\t\t  www.mimosa.co')
if mibBuilder.loadTexts: mimosaMibTC.setContactInfo('postal:\n    \tMimosa Networks, Inc.\n\t\t469 El Camino Real, Suite 100\n\t\tSanta Clara, CA 95050\n        email: support@mimosa.co')
if mibBuilder.loadTexts: mimosaMibTC.setDescription('Mimosa device MIB definitions')
class DecimalOne(TextualConvention, Integer32):
    description = 'Fixed point, one decimal'
    status = 'current'
    displayHint = 'd-1'

class DecimalTwo(TextualConvention, Integer32):
    description = 'Fixed point, two decimals'
    status = 'current'
    displayHint = 'd-2'

class DecimalFive(TextualConvention, Integer32):
    description = 'Fixed point, five decimals'
    status = 'current'
    displayHint = 'd-5'

class Mimosa5GHzFrequency(TextualConvention, Integer32):
    description = 'Represents the frequency in the range of 4800 to 6200'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(4800, 6200)

class Mimosa5GHzChannelNumber(TextualConvention, Integer32):
    description = 'Reprensents the channel Wifi ChannelWidth'
    status = 'current'

mibBuilder.exportSymbols("MIMOSA-MIB-TC", Mimosa5GHzFrequency=Mimosa5GHzFrequency, PYSNMP_MODULE_ID=mimosaMibTC, DecimalFive=DecimalFive, DecimalOne=DecimalOne, DecimalTwo=DecimalTwo, Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, mimosaMibTC=mimosaMibTC)
