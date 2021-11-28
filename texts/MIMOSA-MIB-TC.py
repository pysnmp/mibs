#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.3 at Sun Nov 28 21:12:33 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Bits, Gauge32, NotificationType, Unsigned32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "Gauge32", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32")
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

mibBuilder.exportSymbols("MIMOSA-MIB-TC", DecimalOne=DecimalOne, Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, Mimosa5GHzFrequency=Mimosa5GHzFrequency, mimosaMibTC=mimosaMibTC, DecimalTwo=DecimalTwo, DecimalFive=DecimalFive, PYSNMP_MODULE_ID=mimosaMibTC)
